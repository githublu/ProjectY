from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from Models.Model import *

# this model take text as features and categories as target
# so far only numerical target has been tested
class TfidfPlusClassifierModel(Model):
    def __init__(self, parameter):
        Model.__init__(self, "TfidfPlusClassifierModel")
        parameters = {
            'vect__max_df': (0.5, 0.75, 1.0),
            # 'vect__max_features': (None, 5000, 10000, 50000),
            'vect__ngram_range': ((1, 1), (1, 2)),  # unigrams or bigrams
            # 'tfidf__use_idf': (True, False),
            # 'tfidf__norm': ('l1', 'l2'),
            'clf__alpha': (0.00001, 0.000001),
            'clf__penalty': ('l2', 'elasticnet'),
            # 'clf__n_iter': (10, 50, 80),
        }

        pipeline = Pipeline([
            ('vect', CountVectorizer()),
            ('tfidf', TfidfTransformer()),
            ('clf', SGDClassifier()),
        ])
        self.model = GridSearchCV(pipeline, parameters, n_jobs=-1, verbose=1)
        return

    def fit(self, train_text, train_target):
        self.model.fit(train_text, train_target)
        return

    # give the text tries to cluster
    # return the indedx of the classification
    def predict(self, user_input):
        return self.model.predict(user_input)
