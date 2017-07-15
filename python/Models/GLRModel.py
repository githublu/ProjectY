from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from Models.Model import *


class GLRModel(Model):
    initialParameter = {"degree": 3}

    def __init__(self):
        self.parameter = self.initialParameter
        self.model = Pipeline([('poly', PolynomialFeatures(degree=self.initialParameter["degree"])),('linear', LinearRegression(fit_intercept=False))])


    def set_parameter(self, parameter):
        self.parameter = parameter
        try:
            self.model = Pipeline([('poly', PolynomialFeatures(degree=parameter["degree"])),('linear', LinearRegression(fit_intercept=False))])
        except IndexError:
            log_error("parameter degree does not exit")

    def fit(self, trainingSet, testingSet):
        return self.model.fit(trainingSet, testingSet)

    def predict(self, input):
        return self.model.predict(input)

    def score(self, sourceTestSet, targetTestSet):
        return self.model.score(sourceTestSet, targetTestSet)

    def preprocessing(self, sourceTestSet, targetTestSet):
        return