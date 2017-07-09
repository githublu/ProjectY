from CommonHelper.QueryExec import *

allTypes = {
    "classification": "classification",
    "regression": "regression",
    "invalid": "invalid"
}

class ProblemType:
    type = "invalid"
    def __init__(self, type):
        self.type = type


# return the type of problem
# assumes everything columns are in order
# the last one is target, the rest are features
def GetProblemType(dateTypeQuery, targetName):
    dataTypeTable = ExecQuery(dateTypeQuery)
    dataTypes = {}
    for row in dataTypeTable:
        dataTypes[row[0]] = row[1]
        if row[0] == targetName:
            targetType = row[1]

    if targetType == "int" or targetType == "decimal" or targetType == "float":
        return ProblemType("regression")
    elif targetType == "varchar" or targetType == "bit":
        return ProblemType("classification")
    else:
        return ProblemType("invalid")

# print(GetProblemType("SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS where table_name = 'iris' and TABLE_SCHEMA = 'testdb1'", "species").type)