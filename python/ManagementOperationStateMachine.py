import sys
from sklearn.model_selection import train_test_split
from CommonHelper.QueryExec import *
from Models.RegressionModelManager import *
from Models.ClassificationModelManager import *
from ClusteringStateMachine import *
from Logger.logger import *
from ProblemParser import *
from ModelTuningManager import *

actionOutcome = ""
errorState = 0
totalDataset = []
selectQuery = ""
dataTypeQuery = ""
targetName = ""
sourceDataset = []
targetSet = []
sourceTrainingSet = []
targetTrainingSet = []
sourceTestSet = []
targetTestSet = []
currentBestModel = 0
currentModel = None
currentModelIndex = -1
currentBestScore = -1
modelInput = []
prediction = []
currentModelParameter = 0
modelManager = None
modelTuningManager = None
typeOfProblem = ""
score = 0
totalCounter = 0
testCounts = 0
problemType = None

def EntryPoint(userSelectQuery, userInput, userdataTypeQuery, userTargetName, type="predict"):
    global actionOutcome, selectQuery, modelInput, dataTypeQuery, targetName, problemType
    problemType = type
    selectQuery = userSelectQuery
    dataTypeQuery = userdataTypeQuery
    targetName = userTargetName
    tmpInput = np.array(userInput).reshape(1,-1)[0]
    for v in tmpInput:
        try:
            tmp = float(v)
            modelInput.append(tmp)
        except ValueError:
            modelInput.append(v)

    actionOutcome = "PrecondictionCheck"
    return


def PrecondictionCheck():
    global actionOutcome
    if modelInput is None or selectQuery == "":
        actionOutcome = "FailedPreconditionCheck"
        return

    actionOutcome = "ProblemParsing"
    return

# ProblemParsing determines what type of the question it is. Translate the query into steps
# Regression or classification
# Prediction or abnormality detection
def ProblemParsing():
    global actionOutcome, modelManager, typeOfProblem, modelTuningManager, targetName
    typeOfProblem = GetProblemType(dataTypeQuery, targetName, problemType).type
    if typeOfProblem == "regression":
        modelManager = RegressionModelManager()
    elif typeOfProblem == "classification":
        modelManager = ClassificationModelManager()
    elif typeOfProblem == "clustering":
        actionOutcome = "Prediction"
        return
    else:
        actionOutcome = "InvalidProblemType"
        return

    modelTuningManager = ModelTuningManager()
    actionOutcome = "DataIngestion"
    return


# Reading data from mysql and format into usable format
def DataIngestion():
    global actionOutcome, totalDataset
    totalDataset = GetTable(selectQuery)
    actionOutcome = "ModelSelection"
    return


# Invoke the current model manager to get the next model
# This will always give you a new model
def ModelSelection():
    global actionOutcome, currentModel, currentModelParameter, currentModelIndex
    currentModel = modelManager.next_model()

    # for the last model, go to prediction only
    if currentModel is None and currentBestModel is not None:
        log_debug("run out of models and go to prediction")
        actionOutcome = "Prediction"
        return

    currentModelIndex = modelManager.get_model_index()
    log_debug("current model index %s" % currentModelIndex)

    # first time for this new model
    if typeOfProblem == "clustering":
        #go to new state
        actionOutcome = "ModelTestingAndComparison"
    else:
        actionOutcome = "DataPreprocessing"

    return

# Only preprocess the data once for each new model
# Include splitting dataset into train set and test set
# Call model's function for specific preprocessing
def DataPreprocessing():
    global actionOutcome, sourceDataset, targetSet, sourceTrainingSet, targetTrainingSet, sourceTestSet, targetTestSet
    for X, y in totalDataset:
        sourceDataset = currentModel.preprocessing(X)
        targetSet = currentModel.preprocessing(y)

        sourceTrainingSet, sourceTestSet, targetTrainingSet, targetTestSet = train_test_split(X, y, test_size=.3)

    # skip tuning and use the default parameters
    actionOutcome = "ModelTraining"
    return

# After the first initial parameter prediction, this state determines how should it proceed further
# This is the only state determines if we should keep tuning or choose a new model
def DataTuning():
    global actionOutcome, modelTuningManager, totalCounter
    totalCounter += 1
    if modelTuningManager.keep_tune():
        currentModel.tune()
        actionOutcome = "ModelTraining"
        return
    else:
        actionOutcome = "ModelSelection"
        return


# Run source dataset to train model
def ModelTraining():
    global actionOutcome

    currentModel.fit(sourceTrainingSet, targetTrainingSet)
    actionOutcome = "ModelTestingAndComparison"
    return

# Compare this model with current best model
# Determine if we want to this model is good enough
# Always go back to DataTuning state to determine next step if current model with current parameter is not good enough
def ModelTestingAndComparison():
    global actionOutcome, currentBestScore, currentBestModel, score, testCounts

    if testCounts < 3:
        score += currentModel.score(sourceTestSet, targetTestSet)
        log_debug("attempt %d score is %s" % (testCounts, score/(testCounts+1)))
        testCounts += 1
        actionOutcome = "DataPreprocessing"
        return
    else:
        score /= 3
        testCounts = 0

    modelTuningManager.add_history(modelManager.get_model_index(), currentModel.get_parameter(), score)

    log_debug("current score is %s" % score)
    if score >= currentBestScore:
        currentBestScore = score
        currentBestModel = currentModel

    if score >= 10 or totalCounter > 5:
        score = 0
        actionOutcome = "Prediction"
    else:
        score = 0
        actionOutcome = "DataTuning"
    return

# Once the best model is found, make prediction and return
def Prediction():
    global actionOutcome, prediction

    if typeOfProblem == "clustering":
        # overloading targetName with findCount
        select_queries = ClusteringStateMachineStart(selectQuery, modelInput, targetName)
        CreateClusterOutput(select_queries, targetName)
        return

    if currentBestScore <= 0:
        actionOutcome = "NotAccurate"
    else:
        log_debug("best model is %s" % currentBestModel.get_model_name())
        prediction = currentBestModel.predict(modelInput)
        log_debug(prediction)
        if is_debug() == False:
            CreateOutput(prediction, currentBestScore)

    return

def Start(select_statement, predict_input, schema_statement, target_name):

    FSMStates = {
        "PrecondictionCheck": PrecondictionCheck,
        "ProblemParsing": ProblemParsing,
        "DataIngestion": DataIngestion,
        "ModelSelection": ModelSelection,
        "DataPreprocessing": DataPreprocessing,
        "DataTuning": DataTuning,
        "ModelTraining": ModelTraining,
        "ModelTestingAndComparison": ModelTestingAndComparison,
        "Prediction": Prediction
    }

    FSMSuccessStableState = ["Prediction"]
    FSMFailureStableState = ["NotAccurate", "FailedPreconditionCheck", "InvalidProblemType"]
    FSMStableStates = FSMFailureStableState + FSMSuccessStableState

    # Main entry point
    if is_debug() == False:
        EntryPoint(select_statement,predict_input, schema_statement, target_name)
    else:
        #EntryPoint("select sepal_length, sepal_width, petal_length, petal_width from iris;", ['5.9', '3', '5.1'], "SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS where table_name = 'iris' and TABLE_SCHEMA = 'testdb1'", "petal_width")
        EntryPoint("select sepal_length, sepal_width, petal_length, petal_width, species from iris;", ['5.9', '3', '5.1', '1.8'], "SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS where table_name = 'iris' and TABLE_SCHEMA = 'testdb1'", "species")
        #EntryPoint("select year, population, `violent crime` from crime;", [2014, 326128839],
                   # "SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS where table_name = 'crime' and TABLE_SCHEMA = 'testdb1'",
                   # "violent crime"
                   # )
        #EntryPoint("select sepal_length, sepal_width, petal_length, petal_width from iris;", ['5.9', '3', '5.1', '1.8'], "SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS where table_name = 'iris' and TABLE_SCHEMA = 'testdb1'", 2, "similar")

    while actionOutcome not in FSMStableStates:
        log_debug(actionOutcome)
        FSMStates[actionOutcome]()


    if actionOutcome in FSMSuccessStableState:
        FSMStates[actionOutcome]()
        log_debug("exit successfully")
        exit()
    else:
        log_debug("rollback at state %s" % actionOutcome)
