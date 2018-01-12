from CommonHelper.QueryExec import *
from Constants.ModelType import *

allTypes = {
    "classification": "classification",
    "regression": "regression",
    "clustering": "clustering",
    "invalid": "invalid"
}

# return the type of problem
# assumes everything columns are in order
# the last one is target, the rest are features
def GetProblemType(dateTypeQuery, targetName, type):
    dataTypeTable = ExecQuery(dateTypeQuery)
    dataTypes = {}
    targetType = ""
    if type == "cluster":
        # TODO only support all numeric clustering
        return ModelType.NumericClustering

    for row in dataTypeTable:
        dataTypes[row[0]] = row[1]
        if row[0] == targetName:
            targetType = row[1]

    if targetType == "":
        return ModelType.Invalid

    if targetType == "int" or targetType == "decimal" or targetType == "float":
        return ModelType.Regression
    elif targetType == "varchar" or targetType == "bit":
        for row, data_type in dataTypes.items():
            if row != targetName and data_type == "varchar":
                return ModelType.TextClassification

        return ModelType.NumericClassification
    else:
        return ModelType.Invalid

# print(GetProblemType("SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS where table_name = 'iris' and TABLE_SCHEMA = 'testdb1'", "species").type)