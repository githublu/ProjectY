import abc

class ModelManager:

    @abc.abstractmethod
    def __init__(self):
        self.modelIndex = -1
        self.modelParameter = {}
        self.modelList = []
        return


    def GetModelIndex(self):
        return self.modelIndex


    def GetModelParameter(self):
        return self.modelParameter


    def SetModelIndex(self, index):
        self.modelIndex = index

    @abc.abstractmethod
    def next_model(self):
        return

    @abc.abstractmethod
    def get_model(self, model, parameters):
        return