# The purpose of this manager is to determin when should it keep tuning the model
# or this model is in local optimal and should tr next one

class ModelTuningManager():

    history = {}
    attempt = 0

    def __init__(self):
        return

    def add_history(self, model_name, parameters, score):
        self.history[model_name][self.attempt] = [parameters, score]

    def keep_tune(self):
        return False;