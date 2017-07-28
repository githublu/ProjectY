
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn import datasets
import uuid
import pymysql
import datetime
import sys
import pickle as pickle
from sklearn import svm

irisDatasets = datasets.load_iris()
dataset = []
tup = ()
data = np.array(irisDatasets.data)
target = np.array(irisDatasets.target)
tup += data,
tup += target,
dataset.append(tup)

clf = svm.SVR()
for X, y in dataset:
    #X = StandardScaler().fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    score = clf.score(X_test, y_test)
    print(y_test)
    print(predictions)
    print(score)

