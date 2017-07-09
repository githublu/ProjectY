
class Model:
    type = ""
    model = None
    def __init__(self):
        self.type = ""
        self.model = None

    def fit(self, trainingSet, testingSet):
        return self.model.fit(trainingSet, testingSet)

    def predict(self, input):
        return self.model.predict(input)

    def score(self, sourceTestSet, targetTestSet):
        return self.model(sourceTestSet, targetTestSet)