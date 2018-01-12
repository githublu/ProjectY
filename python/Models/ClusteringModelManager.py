import json
from Models.ModelManager import ModelManager
from Models.NearestNeighbors import *
from Logger.logger import *

class ClusteringModelManager(ModelManager):
    def __init__(self):
        ModelManager.__init__(self)
        # D:\Projects\ProjectY\python\ModelConfig\model.json
        # /Users/yilu/Projects/mysql-server/python/ModelConfig/model.json
        with open('D:\Projects\ProjectY\python\ModelConfig\model.json') as model_config_file:
            model_config_all = json.load(model_config_file)

        self.model_config = model_config_all["Clustering"]
        self.modelList = self.model_config["ModelList"]

# no-ops
    def next_model(self):
        return

    def get_model(self, model_name, parameters):
        for model in self.modelList:
            if model == model_name:
                self.modelParameter = self.model_config["InitialParameters"][model]
                return NearestNeighborsModel(self.modelParameter)


