import numpy as np
from sklearn import svm
from Models.Model import *

class SVMModel(Model):

    def __init__(self, parameter):
        self.parameter = parameter
        self.model = svm.SVR()

    def set_parameter(self, parameters):
        return

    def fit(self, trainingSet, testingSet):
        return self.model.fit(trainingSet, testingSet)

    def predict(self, input):
        return self.model.predict(input)

    def score(self, sourceTestSet, targetTestSet):
        return self.model.score(sourceTestSet, targetTestSet)

    def preprocessing(self, dataset):
        return dataset

    def tune(self):
        return
