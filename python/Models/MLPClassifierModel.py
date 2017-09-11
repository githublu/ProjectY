from sklearn.neural_network import MLPClassifier
from Models.Model import *
from ast import literal_eval

class MLPClassifierModel(Model):

    def __init__(self, parameter):
        Model.__init__(self, "MLPClassifierModel")
        self.parameter = parameter
        self.solver_index = self.parameter["solver_index"]
        self.model = MLPClassifier(solver=self.parameter["solver"][self.solver_index], alpha=self.parameter["alpha"],
                                   hidden_layer_sizes=literal_eval(self.parameter["hidden_layer_sizes"]), random_state=self.parameter["random_state"])

    def set_parameter(self, parameter):
        self.parameter = parameter
        try:
            self.model = MLPClassifier(solver=self.parameter["solver"][self.solver_index], alpha=self.parameter["alpha"],
                                       hidden_layer_sizes=literal_eval(self.parameter["hidden_layer_sizes"]), random_state=self.parameter["random_state"])
        except IndexError:
            log_error(IndexError)

    def fit(self, training_set, testing_set):
        return self.model.fit(training_set, testing_set)

    def predict(self, user_input):
        return self.model.predict(user_input)

    def score(self, source_test_set, target_test_set):
        return self.model.score(source_test_set, target_test_set)

    def preprocessing(self, dataset):
        return dataset

    def tune(self):
        self.solver_index += 1
        try:
            self.model = MLPClassifier(solver=self.parameter["solver"][self.solver_index], alpha=self.parameter["alpha"],
                                       hidden_layer_sizes=literal_eval(self.parameter["hidden_layer_sizes"]),
                                       random_state=self.parameter["random_state"])
        except IndexError:
            log_debug("end of solver")

        return
