from sklearn.linear_model import Perceptron
from Models.Model import *


class PerceptronModel(Model):

    initialParameter = {"n_iter": 3}

    def __init__(self, parameters):
        self.parameters = self.initialParameter
        self.model = Perceptron(n_iter=self.initialParameter["n_iter"])

    def set_parameter(self, parameters):
        self.parameters = parameters
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
        self.parameters["n_iter"] += 1
        self.model = Perceptron(n_iter=self.parameters["n_iter"])
        return
