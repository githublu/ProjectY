from sklearn.linear_model import Perceptron
from Models.Model import *
import numpy as np


class PerceptronModel(Model):

    # initialParameter = {"n_iter": 3}

    def __init__(self, parameters):
        self.parameter = parameters
        self.model = Perceptron(n_iter=self.parameter["n_iter"])

    def set_parameter(self, parameters):
        self.parameter = parameters
        try:
            self.model = Perceptron(n_iter=parameters["n_iter"])
        except IndexError:
            raise ValueError("parameter %s does not exit" % "n_iter")


    def fit(self, source_training_set, starget_training_set):
        return self.model.fit(source_training_set, np.asanyarray(starget_training_set))

    def predict(self, input):
        return self.model.predict(input)

    def score(self, sourceTestSet, targetTestSet):
        return self.model.score(sourceTestSet, targetTestSet)

    def preprocessing(self, dataset):
        return dataset

    def tune(self):
        self.parameter["n_iter"] += 1
        self.model = Perceptron(n_iter=self.parameter["n_iter"])
        return
