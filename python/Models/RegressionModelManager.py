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
        with open('D:\Projects\ProjectY\python\ModelConfig\model.json') as model_config_file:
            self.model_config = json.load(model_config_file)

        self.modelList = self.model_config["ModelList"]

    def next_model(self):
        self.SetModelIndex(self.modelIndex + 1)
        return self.get_model(self.modelIndex)

    def get_model(self, model):
        try:
            model = self.modelList[model]
            parameters = self.model_config["InitialParameters"][model]
            if model == "SVMModel":
                return SVMModel(parameters)
            elif model == "GLR":
                return GLRModel(parameters)
            elif model == "PerceptionModel":
                return PerceptronModel(parameters)
        except IndexError:
            return None
        except ValueError as error:
            log_warning(repr(error))
