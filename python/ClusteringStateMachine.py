from Logger.logger import *
from CommonHelper.QueryExec import *
from Models.ClusteringModelManager import *

# global variable
actionOutcome = None
selectQuery = ""
modelManager = None
currentModel = None
sampleDataset = None
finalQuery = None

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

    if findCount <= 0:
        actionOutcome = "NegativeOrZeroRow"
        return
    if reference is None or reference == "":
        actionOutcome = "NoReference"

    actionOutcome = "DataIngestion"
    return

def DataIngestion():
    global actionOutcome, sampleDataset
    sampleDataset = GetClusteringTable(selectQuery)
    actionOutcome = "ModelSelection"
    return

# needs to determine which model to use
def ModelSelection():
    global actionOutcome, currentModel
    # TODO: determine which model need to be used

    # currently only Nearest Neighbors is supported
    # if all fields are numerical
    # or if fields are categorical, then convert them into 0,1 columns
    currentModel = ClusteringModelManager().get_model("NearestNeighborsModel", None)

    # if the text field is not categorical and find similar text document
    # use TFIDF to lable them and select similar ones

    # fit model
    currentModel.fit(sampleDataset)

    actionOutcome = "FindSimilar"
    return

# return final prediction result
def FindSimilar():
    global findCount, currentModel, finalQuery
    outputs = []
    similar_indices = currentModel.predict_count(reference, findCount)

    for i in similar_indices:
        outputs.append(sampleDataset[i])

    query = "SELECT * FROM "

    # get a list of parameters
    index_of_from = selectQuery.find("from")
    all_params = selectQuery[6: index_of_from].split(",")
    table_name = selectQuery[index_of_from + 5:selectQuery.find(" ", index_of_from + 5)]
    is_first = True
    query += table_name + " WHERE "
    tmp_query = query
    queries = []
    for output in outputs:
        for i in range(0, len(all_params)):
            if is_first:
                tmp_query += str(all_params[i]) + " = " + str(output[i])
                is_first = False
            else:
                tmp_query += " AND " + str(all_params[i]) + " = " + str(output[i])

        queries.append(tmp_query)
        tmp_query = query
        is_first = True

    CreateClusterOutput(queries, findCount)


# entry point
def ClusteringStateMachineStart(userSelectQuery, userModelInput, count):
    # define all the states
    FSMStates = {
        "DataIngestion": DataIngestion,
        "ModelSelection": ModelSelection,
        "FindSimilar": FindSimilar
    }

    # define stable states
    FSMSuccessStableState = ["FindSimilar"]
    FSMFailureStableState = ["NegativeOrZeroRow", "NoReference"]
    FSMStableStates = FSMFailureStableState + FSMSuccessStableState

    # entering the first state
    PrecondictionCheck(userSelectQuery, userModelInput, count)

    while actionOutcome not in FSMStableStates:
        log_debug(actionOutcome)
        FSMStates[actionOutcome]()

    if actionOutcome in FSMSuccessStableState:
        log_debug("exit ClusteringStateMachine successfully at state %s" % actionOutcome)
        FSMStates[actionOutcome]()
    else:
        log_debug("rollback at state %s" % actionOutcome)

    return
