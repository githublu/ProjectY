from enum import Enum
class ModelType(Enum):
        Invalid = 0
        Regression = 1
        NumericClassification = 2
        TextClassification = 3
        NumericClustering = 4
        TextClustering = 5