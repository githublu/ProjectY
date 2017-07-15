import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix
import pymysql
import pickle as pickle
from sklearn.preprocessing import PolynomialFeatures
from CommonHelper.QueryExec import *
from Models.RegressionModelManager import *
from Models.ClassificationModelManager import *
from Logger.logger import *
from ProblemParser import *
from sklearn import svm

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
tunningCounter = 0
modelManager = None
typeOfProblem = ""

def EntryPoint(userSelectQuery, userInput, userdataTypeQuery, userTargetName):
    global actionOutcome, selectQuery, modelInput, dataTypeQuery, targetName
    log_debug("function enter: EntryPoint")
    selectQuery = userSelectQuery
    dataTypeQuery = userdataTypeQuery
    targetName = userTargetName
    modelInput = np.array(userInput).reshape(1,-1)

    actionOutcome = "PrecondictionCheck"
    return

def PrecondictionCheck():
    global actionOutcome
    if modelInput == [] or selectQuery == "":
        actionOutcome = "FailedPreconditionCheck"
        return

    actionOutcome = "DataInjestion"
    return


# Reading data from mysql and format into usable format
def DataInjestion():
    global actionOutcome, totalDataset
    log_debug("function enter: DataInjestion")
    totalDataset = GetTable(selectQuery)
    actionOutcome = "ProblemParsing"
    return


# ProblemParsing determines what type of the question it is. Translate the query into steps
# Regression or classification
# Prediction or abnormality detection
def ProblemParsing():
    global actionOutcome, modelManager, typeOfProblem
    typeOfProblem = GetProblemType(dataTypeQuery, targetName).type
    if typeOfProblem == "regression":
        modelManager = RegressionModelManager()
    elif typeOfProblem  == "classification":
        modelManager = ClassificationModelManager()

    actionOutcome = "ModelSelection"
    return


# Select a range to best model for this problem
# Decide whether keep tuning current model or switch to next model
def ModelSelection():
    global actionOutcome, currentModel, currentModelParameter, currentModelIndex
    log_debug("doing ModelSelection")
    currentModel = modelManager.next_model()
    if currentModel is None:
        actionOutcome = "Prediction"
        return

    #currentModel = regressionModelManager.GetModel(1, 3)
    currentModelIndex = modelManager.GetModelIndex()
    currentModelParameter = modelManager.GetModelParameter()
    log_info("current model index %s" % currentModelIndex)
    actionOutcome = "DataTuningAndPreprocessing"
    return


# Preprocess dataset to certain transformation to be better fit
def DataTuningAndPreprocessing():
    global actionOutcome, sourceDataset, targetSet, sourceTrainingSet, targetTrainingSet, sourceTestSet, targetTestSet
    log_debug("doing preprocessing")
    for X, y in totalDataset:
        sourceDataset = X

        # sourceDataset = StandardScaler().fit_transform(sourceDataset)
        targetSet = y
        sourceTrainingSet, sourceTestSet, targetTrainingSet, targetTestSet = train_test_split(X, y, test_size=.3)
    actionOutcome = "ModelTraining"
    return

# Run source dataset to train model
def ModelTraining():
    global actionOutcome
    log_debug("doing ModelTraining")
    currentModel.fit(sourceTrainingSet, targetTrainingSet)
    actionOutcome = "ModelTestingAndComparison"
    return

# Compare this model with current best model
# Determine if we want to tune current model or try next one
def ModelTestingAndComparison():
    global actionOutcome, currentBestScore, currentBestModel
    log_debug("doing ModelTestingAndComparison")
    score = currentModel.score(sourceTestSet, targetTestSet)
    log_debug("current score is %s" % score)
    if score >= currentBestScore:
        currentBestScore = score
        currentBestModel = currentModel

    if score >= 0.5:
        actionOutcome = "Prediction"
    elif score >= 0.2:
        actionOutcome = "DataTuningAndPreprocessing"
    else:
        actionOutcome = "ModelSelection"
    return

# Once the best model is found, make prediction and return
def Prediction():
    global actionOutcome, prediction
    log_debug("doing Prediction")
    if currentBestScore <= 0:
        actionOutcome = "NotAccurate"
    else:
        prediction = currentBestModel.predict(modelInput)
        log_debug(prediction)

    return


FSMStates = {
    "PrecondictionCheck": PrecondictionCheck,
    "ProblemParsing": ProblemParsing,
    "DataInjestion": DataInjestion,
    "ModelSelection": ModelSelection,
    "DataTuningAndPreprocessing": DataTuningAndPreprocessing,
    "ModelTraining": ModelTraining,
    "ModelTestingAndComparison": ModelTestingAndComparison,
    "Prediction": Prediction
}

FSMSuccessStableState = ["Prediction"]
FSMFailureStableState = ["NotAccurate", "FailedPreconditionCheck"]
FSMStableStates = FSMFailureStableState + FSMSuccessStableState


# # main entry point
## example of using MLPClassifier
#EntryPoint("select * from iris;", [5.9, 3, 5.1, 1.8], "SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS where table_name = 'iris' and TABLE_SCHEMA = 'testdb1'", "species")
EntryPoint("select year, population, `violent crime` from crime;", [2014, 326128839],
           "SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS where table_name = 'crime' and TABLE_SCHEMA = 'testdb1'",
           "violent crime"
           )
while actionOutcome not in FSMStableStates:
    log_debug(actionOutcome)
    FSMStates[actionOutcome]()


if actionOutcome in FSMSuccessStableState:
    FSMStates[actionOutcome]()
    log_info("exit successfully")
    exit()
else:
    log_info("rollback at state %s" % actionOutcome)
