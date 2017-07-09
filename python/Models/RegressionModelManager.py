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


class RegressionModelManager(ModelManager):

    def __init__(self):
        super().__init__()
        self.modelList = ["svm", "GLR"]

    def NextModel(self):
        self.SetModelIndex(self.modelIndex + 1)
        return self.GetModel(self.modelIndex, self.modelParameter)

    def GetModel(self, model, parameters):
        try:
            if self.modelList[model] == "svm":
                return svm.SVR()
            elif self.modelList[model] == "GLR":
                return Pipeline([('poly', PolynomialFeatures(degree=parameters)),('linear', LinearRegression(fit_intercept=False))])
        except IndexError:
            return None
