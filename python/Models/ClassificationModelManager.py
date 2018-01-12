import numpy as np
from Models.ModelManager import ModelManager
from Models.PerceptronModel import *
from Models.MLPClassifierModel import *
import json
from Constants.ModelType import *

class ClassificationModelManager(ModelManager):
    modelIndex = -1
    type = ModelType.NumericClassification;

    def __init__(self, model_type):
        ModelManager.__init__(self)
        # D:\Projects\ProjectY\python\ModelConfig\model.json
        # /Users/yilu/Projects/mysql-server/python/ModelConfig/model.json
        with open('D:\Projects\ProjectY\python\ModelConfig\model.json') as model_config_file:
            model_config_all = json.load(model_config_file)

        self.model_config = model_config_all["Classification"]
        self.modelList = self.model_config["ModelList"]
        self.type = model_type

    def next_model(self):
        self.set_model_index(self.modelIndex + 1)
        return self.get_model(self.modelIndex, None)

    def get_model(self, model_index, parameters):
        try:
            model = self.modelList[model_index]
            if parameters is None:
                parameters = self.model_config["InitialParameters"][model]

            if model == "PerceptionModel":
                #return MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100, 100, 100, 100), random_state=1)
                return PerceptronModel(parameters)
            elif model == "MLPClassifierModel":
                return MLPClassifierModel(parameters)
        except IndexError:
            return None
