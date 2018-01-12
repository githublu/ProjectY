import sys
from sklearn.model_selection import train_test_split
from CommonHelper.QueryExec import *
from Constants.ModelType import *
from Models.RegressionModelManager import *
from Models.ClassificationModelManager import *
from ClusteringStateMachine import *
from Logger.logger import *
from ProblemParser import *
from ModelTuningManager import *
from CommonHelper.ModelCache import *

actionOutcome = ""
errorState = 0
totalDataset = []
selectQuery = ""
dataTypeQuery = ""
targetName = ""
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
problemType = "predict"
testSplitSize = 0.3
findCount = 1

def EntryPoint(userSelectQuery, userInput, userdataTypeQuery, userTargetName, type, count):
    global actionOutcome, selectQuery, modelInput, dataTypeQuery, targetName, problemType, findCount
    if type == "cluster":
        problemType = type
        findCount = count

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

    actionOutcome = "PreconditionCheck"
    return


def PreconditionCheck():
    global actionOutcome
    if modelInput is None or selectQuery == "":
        actionOutcome = "FailedPreconditionCheck"
        return

    actionOutcome = "ProblemParsing"
    return

# ProblemParsing determines what type of the question it is. Translate the query into steps
# Regression or classification or Clustering or Abnormality detection
# Apply model cache
def ProblemParsing():
    global actionOutcome, modelManager, typeOfProblem, modelTuningManager, targetName, currentBestModel

    # if there is existing model for this problem
    cached_model = GetCachedModel(selectQuery+problemType)
    if cached_model != False:
        currentBestModel = cached_model
        actionOutcome = "Prediction"
        return

    typeOfProblem = GetProblemType(dataTypeQuery, targetName, problemType)
    if typeOfProblem == ModelType.Regression:
        modelManager = RegressionModelManager()
    elif typeOfProblem == ModelType.NumericClassification or typeOfProblem == ModelType.TextClassification:
        modelManager = ClassificationModelManager(typeOfProblem)

        # TODO: or it is text document classification, current only numeric classification is supported
        # set currentBestScore = 1 so it can just go to prediction
        # set testSplitSize = 1

    # if there is no cached model and it is clustering problem
    # that use ClusteringStateMachine instead of current statemachine
    elif typeOfProblem == ModelType.NumericClustering or typeOfProblem == ModelType.TextClustering:
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
    actionOutcome = "DataPreprocessing"

    return

# Only preprocess the data once for each new model
# Include splitting dataset into train set and test set
# Call model's function for specific preprocessing
def DataPreprocessing():
    global actionOutcome, sourceTrainingSet, targetTrainingSet, sourceTestSet, targetTestSet
    for X, y in totalDataset:
        sourceTrainingSet, sourceTestSet, targetTrainingSet, targetTestSet = train_test_split(X,
                                                                                              y,
                                                                                              test_size=testSplitSize)

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
# or apply cached model
def Prediction():
    global actionOutcome, prediction

    # determine if it should be prediction of this statemachine or other statemachine
    if typeOfProblem == ModelType.NumericClustering:
        # overloading targetName with findCount
        ClusteringStateMachineStart(selectQuery, modelInput, findCount)

        return

    # if the type fo the problem is not clustering, then it must use the regular statemachine
    # classification or regression problem
    if currentBestScore <= 0:
        actionOutcome = "NotAccurate"
    else:
        log_debug("best model is %s" % currentBestModel.get_model_name())
        prediction = currentBestModel.predict(modelInput)
        CacheModel(selectQuery + problemType, currentBestModel)
        log_debug(prediction)
        if is_debug() == False:
            CreateOutput(prediction, currentBestScore)

    return

def Start(select_statement, predict_input, schema_statement, target_name, problem_type):

    FSMStates = {
        "PreconditionCheck": PreconditionCheck,
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
        EntryPoint(select_statement,predict_input, schema_statement, target_name, problem_type)
    else:
        #EntryPoint("select sepal_length, sepal_width, petal_length, petal_width from iris;", ['5.9', '3', '5.1'], "SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS where table_name = 'iris' and TABLE_SCHEMA = 'testdb1'", "petal_width")

        # regressions model test
        #EntryPoint("select sepal_length, sepal_width, petal_length, petal_width, species from iris;", ['5.9', '3', '5.1', '1.8'], "SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS where table_name = 'iris' and TABLE_SCHEMA = 'testdb1'", "species", "predict")

        # clustering model test
        EntryPoint("select sepal_length, sepal_width, petal_length, petal_width from iris;",
                   ['5.9', '3', '5.1', '1.8'],
                   "SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS where table_name = 'iris' and TABLE_SCHEMA = 'testdb1'","", "cluster", 2)
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
