from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from Models.Model import *

class TfidfPlusClassifierModel(Model):
    def __init__(self, parameter):
        Model.__init__(self, "TfidfPlusClassifierModel")
        pipeline = None
        self.model = pipeline
        return

    def set_parameter(self, parameter):
        return

    def fit(self, training_set, testing_set):
        return

    def predict(self, input):
        return

    def score(self, source_test_set, target_test_set):
        return

    def preprocessing(self, dataset):
        return dataset

    def tune(self):
        return False