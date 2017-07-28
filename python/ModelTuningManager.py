# The purpose of this manager is to determine when should it keep tuning the model
# or this model is in local optimal and should tr next one
# return the new set of parameters

class ModelTuningManager():

    history = {0: {}}
    attempt = 0

    def __init__(self):
        return

    def add_history(self, model_index, parameters, score):
        self.history[model_index] = {}
        self.history[model_index][self.attempt] = [parameters, score]

    def keep_tune(self):
        return False

    def next_parameter(self):
        return []