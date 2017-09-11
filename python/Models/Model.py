import abc
from Logger.logger import *

class Model(object):

    model = None
    parameter = []
    model_name = ""

    @abc.abstractmethod
    def __init__(self, model_name):
        self.model_name = model_name
        return

    @abc.abstractmethod
    def set_parameter(self, parameters):
        return

    @abc.abstractmethod
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

    def get_model_name(self):
        return self.model_name
