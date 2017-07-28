import abc

class ModelManager:

    def __init__(self):
        self.modelIndex = -1
        self.modelParameter = {}
        self.modelList = []
        return


    def get_model_index(self):
        return self.modelIndex


    def set_model_index(self, index):
        self.modelIndex = index

    @abc.abstractmethod
    def next_model(self):
        return

    @abc.abstractmethod
    def get_model(self, model, parameters):
        return