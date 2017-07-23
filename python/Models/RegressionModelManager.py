import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
import numpy as np
from sklearn import svm
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from Models.ModelManager import ModelManager
from Models.SVMModel import *
from Models.PerceptronModel import *
from Models.GLRModel import *
import json


class RegressionModelManager(ModelManager):

    def __init__(self):
        ModelManager.__init__(self)
        with open('/Users/yilu/Projects/mysql-server/python/ModelConfig/model.json') as model_config_file:
            self.model_config = json.load(model_config_file)

        self.modelList = self.model_config["modelList"]

    def next_model(self):
        self.SetModelIndex(self.modelIndex + 1)
        return self.get_model(self.modelIndex, self.modelParameter)

    def get_model(self, model, parameters):
        try:
            if self.modelList[model] == "SVMModel":
                return SVMModel(parameters)
            elif self.modelList[model] == "GLR":
                return GLRModel(parameters)
            elif self.modelList[model] == "PerceptionModel":
                return PerceptronModel(parameters)
        except IndexError:
            return None
        except ValueError as error:
            log_warning(repr(error))
