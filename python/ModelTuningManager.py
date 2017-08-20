# The purpose of this manager is to determine when should it keep tuning the model
# or this model is in local optimal and should tr next one
# return the new set of parameters

class ModelTuningManager():

    history = {}
    attempt = 0
    current_model_index = -1
    current_max_score = -1

    def __init__(self):
        return

    def add_history(self, model_index, parameters, score):
        if self.history.__contains__(model_index):
            self.attempt += 1
        else:
            self.attempt = 0
            self.history[model_index] = {}

        self.history[model_index][self.attempt] = [parameters, score]
        self.current_model_index = model_index

    # if every model will tune once
    # if the it get better, keep tune
    # if it get worse, do not keep tune
    def keep_tune(self):
        if self.current_model_index == -1:
            return False
        else:
            model_history = self.history[self.current_model_index]

            local_max_score = -1
            for attempt, value in sorted(model_history.items()):
                current_score = value[1]
                if current_score <= local_max_score:
                    return False
                else:
                    local_max_score = current_score

        return True
