import numpy as np
from sklearn.neighbors import NearestNeighbors
from Models.Model import *


class NearestNeighborsModel:

    model = None
    parameter = []
    model_name = ""
    kneighbors = None

    def __init__(self, parameters):
        self.model_name = "NearestNeighborsModel"
        self.parameter = parameters
        #NearestNeighbors(n_neighbors=3, algorithm='ball_tree')
        self.model = NearestNeighbors(n_neighbors=self.parameter["n_neighbors"],
                                      algorithm=self.parameter["algorithm"])

    def set_parameter(self, parameter):
        self.parameter = parameter
        try:
            self.model = NearestNeighbors(n_neighbors=self.parameter["n_neighbors"],
                                          algorithm=self.parameter["algorithm"])
        except IndexError:
            log_error("parameter degree does not exit")

    def fit(self, training_set):
        # distance, indices = self.model.kneighbors(input)
        # self.kneighbors = indices
        return self.model.fit(training_set)

    def predict_count(self, reference, count):
        # from the kneighbors, find all the similar rows in the table up to counts
        # return indices of similar entries
        return self.model.kneighbors(reference, count)[1][0]

    def get_model_name(self):
        return self.model_name
