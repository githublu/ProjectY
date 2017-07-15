import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
import numpy as np
from Models.ModelManager import ModelManager


class ClassificationModelManager(ModelManager):
    modelIndex = -1

    def __init__(self):
        super().__init__()
        self.modelList = ["MLPClassifier"]

    def next_model(self):
        self.SetModelIndex(self.modelIndex + 1)
        return self.GetModel(self.modelIndex, self.modelParameter)

    def get_model(self, model, parameters):
        try:
            if self.modelList[model] == "MLPClassifier":
                return MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100, 100, 100, 100), random_state=1)
        except IndexError:
            return None