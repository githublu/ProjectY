from sklearn.linear_model import Perceptron
from Models.Model import *


class PerceptronModel(Model):

    # initialParameter = {"n_iter": 3}

    def __init__(self, parameters):
        self.parameter = parameters
        self.model = Perceptron(n_iter=self.initialParameter["n_iter"])

    def set_parameter(self, parameters):
        self.parameter = parameters
        try:
            self.model = Perceptron(n_iter=parameters["n_iter"])
        except IndexError:
            raise ValueError("parameter %s does not exit" % "n_iter")


    def fit(self, trainingSet, testingSet):
        return self.model.fit(trainingSet, testingSet)

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
