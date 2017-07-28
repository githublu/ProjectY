import numpy as np
from Models.ModelManager import ModelManager
from Models.SVMModel import *
from Models.PerceptronModel import *
from Models.GLRModel import *
import json


class RegressionModelManager(ModelManager):

    def __init__(self):
        ModelManager.__init__(self)
        # D:\Projects\ProjectY\python\ModelConfig\model.json
        # /Users/yilu/Projects/mysql-server/python/ModelConfig/model.json
        with open('D:\Projects\ProjectY\python\ModelConfig\model.json') as model_config_file:
            model_config_all = json.load(model_config_file)

        self.model_config = model_config_all["Regression"]
        self.modelList = self.model_config["ModelList"]


    def next_model(self):
        self.set_model_index(self.modelIndex + 1)
        return self.get_model(self.modelIndex, None)

    def get_model(self, modelIndex, parameters):
        try:
            model = self.modelList[modelIndex]
            if parameters is None:
                parameters = self.model_config["InitialParameters"][model]
            if model == "SVMModel":
                return SVMModel(parameters)
            elif model == "GLR":
                return GLRModel(parameters)
            elif model == "PerceptionModel":
                return PerceptronModel(parameters)
        except IndexError:
            return None
        except ValueError as error:
            log_warning(repr(error))
