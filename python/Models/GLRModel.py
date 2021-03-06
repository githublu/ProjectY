from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from Models.Model import *


class GLRModel(Model):

    def __init__(self, parameters):
        Model.__init__(self, "GLRModel")
        self.parameter = parameters
        self.model = Pipeline([('poly', PolynomialFeatures(degree=self.parameter["degree"])),('linear', LinearRegression(fit_intercept=False))])

    def set_parameter(self, parameter):
        self.parameter = parameter
        try:
            self.model = Pipeline([('poly', PolynomialFeatures(degree=parameter["degree"])), ('linear', LinearRegression(fit_intercept=False))])
        except IndexError:
            log_error("parameter degree does not exit")

    def fit(self, trainingSet, testingSet):
        return self.model.fit(trainingSet, testingSet)

    def predict(self, input):
        return self.model.predict(input)

    def score(self, sourceTestSet, targetTestSet):
        return self.model.score(sourceTestSet, targetTestSet)

    def preprocessing(self, dataset):
        return dataset

    def tune(self):
        self.parameter["degree"] += 1
        self.model = Pipeline([('poly', PolynomialFeatures(degree=self.parameter["degree"])),
                               ('linear', LinearRegression(fit_intercept=False))])
        return
