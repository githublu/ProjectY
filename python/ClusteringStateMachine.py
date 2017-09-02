from Logger.logger import *
from CommonHelper.QueryExec import *
from Models.ClusteringModelManager import *

# global variable
actionOutcome = None
selectQuery = ""
modelManager = None
currentModel = None
sampleDataset = None

# how many similar entries user wants to find
findCount = 1

# find similar row to this one
reference = None

# states
def PrecondictionCheck(userSelectQuery, userReference, userFindCount):
    global actionOutcome, selectQuery, findCount, reference
    selectQuery = userSelectQuery
    findCount = userFindCount
    reference = userReference

    actionOutcome = "DataIngestion"
    return

def DataIngestion():
    global actionOutcome, sampleDataset
    sampleDataset = GetTable(selectQuery)
    actionOutcome = "ModelSelection"
    return

# needs to determine which model to use
def ModelSelection():
    global actionOutcome
    # TODO: determine which model need to be used

    # currently only Nearest Neighbors is supported
    currentModel = ClusteringModelManager().get_model(NearestNeighborsModel, None)
    currentModel.fit(sampleDataset)

    actionOutcome = "FindSimilar"
    return

# return final prediction result
def FindSimilar():
    global findCount
    output = []
    similar_indices = currentModel.predict_count(reference, findCount)

    for i in similar_indices:
        output.append(sampleDataset[i])

    return output


# entry point
def Start(userSelectQuery, userTargetName, userModelInput):
    # define all the states
    FSMStates = {
        "DataInjestion": DataIngestion,
        "ModelSelection": ModelSelection,
        "FindSimilar": FindSimilar
    }

    # define stable states
    FSMSuccessStableState = ["FindSimilar"]
    FSMFailureStableState = ["NotAccurate", "FailedPreconditionCheck", "InvalidProblemType"]
    FSMStableStates = FSMFailureStableState + FSMSuccessStableState

    # entering the first state
    PrecondictionCheck(userSelectQuery, userTargetName, userModelInput)

    while actionOutcome not in FSMStableStates:
        log_debug(actionOutcome)
        FSMStates[actionOutcome]()

    if actionOutcome in FSMSuccessStableState:
        log_debug("exit ClusteringStateMachine successfully")
        return FSMStates[actionOutcome]()
    else:
        log_debug("rollback at state %s" % actionOutcome)

    return
