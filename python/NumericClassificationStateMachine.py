from Logger.logger import *
from CommonHelper.QueryExec import *
from Models.ClusteringModelManager import *
from enum import Enum

class FSMStates(Enum):
    PreconditionCheck = 0,
    DataIngestion = 1,
    DataPreprocessing = 2,
    ModelSelection = 3,
    PredictClassification = 4

# global variable
actionOutcome = None

# states
def PreconditionCheck(userSelectQuery, userReference):
    global actionOutcome

    actionOutcome = FSMStates.DataIngestion
    return

def DataIngestion():
    global actionOutcome

    actionOutcome = FSMStates.DataPreposcessing
    return

def DataPreprocessing():
    return

# needs to determine which model to use
def ModelSelection():
    return

def PredictClassification():
    return

def NumericClassificationStateMachineStart(userSelectQuery, userModelInput):
    # define all the states
    StatesToFunction = {
        FSMStates.DataIngestion: DataIngestion,
        FSMStates.DataPreposcessing: DataPreprocessing,
        FSMStates.ModelSelection: ModelSelection,
        FSMStates.PredictClassification: PredictClassification
    }

    # define stable states
    FSMSuccessStableState = [FSMStates.PredictClassification]
    FSMFailureStableState = ["NegativeOrZeroRow", "NoReference"]
    FSMStableStates = FSMFailureStableState + FSMSuccessStableState

    # entering the first state
    PreconditionCheck(userSelectQuery, userModelInput)

    while actionOutcome not in FSMStableStates:
        log_debug(actionOutcome)
        StatesToFunction[actionOutcome]()

    if actionOutcome in FSMSuccessStableState:
        log_debug("exit NumericClassificationStateMachine successfully at state %s" % actionOutcome)
        FSMStates[actionOutcome]()
    else:
        log_debug("rollback at state %s" % actionOutcome)

    return

NumericClassificationStateMachineStart("", "")