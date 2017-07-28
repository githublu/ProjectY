import abc
from Logger.logger import *

class Model(object):

    model = None
    parameter = []

    @abc.abstractmethod
    def __init__(self):
        return

    @abc.abstractmethod
    def set_parameter(self, parameters):
        return

    def get_parameter(self):
        return self.parameter

    @abc.abstractmethod
    def fit(self, trainingSet, testingSet):
        return

    @abc.abstractmethod
    def predict(self, input):
        return

    @abc.abstractmethod
    def score(self, sourceTestSet, targetTestSet):
        return

    @abc.abstractmethod
    def preprocessing(self, dataset):
        return

    @abc.abstractmethod
    def tune(self):
        return
