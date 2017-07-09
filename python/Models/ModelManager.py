class ModelManager:
    modelIndex = -1
    modelParameter = 3
    modelList = []


    def __init__(self):
        # self.modelIndex = -1
        # self.modelParameter = 3
        # self.modelList = []
        return

    def GetModelIndex(self):
        return self.modelIndex

    def GetModelParameter(self):
        return self.modelParameter

    def SetModelIndex(self, index):
        self.modelIndex = index

mm = ModelManager()
mm.SetModelIndex(2)
print(mm.modelIndex)