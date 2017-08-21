# Author: Issam H. Laradji
# License: BSD 3 clause

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

hostname = 'localhost'
username = 'root'
password = ''
database = 'testdb1'

# # Simple routine to run a query on a database and print the results:
def ExecQuery( conn, query) :
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()


#datasets = [make_moons(noise=0.3, random_state=0)]
irisDatasets = datasets.load_iris()

sample = []
tup = ()
data = np.array(irisDatasets.data)
target = np.array(irisDatasets.target)
tup += data,
tup += target,
sample.append(tup)

#print(sample)
#print(irisDatasets.target_names)

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100, 100, 100, 100), random_state=1)



dbConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )

## create temp table with feature and score
tableName = str(uuid.uuid4()).replace('-', '0')

selectResutlQuery = "select * from iris;"
cur = dbConnection.cursor()
cur.execute(selectResutlQuery)
i = 2
dataset = []
data = []
target = []
tup = ()
for row in cur:
    targetR = row[len(row)-1]
    target.append(targetR)
    row = row[:-1]
    dataR = []
    for r in row:
        dataR.append(r)

    data.append(dataR)

data = np.array(data)
target = np.array(target)
tup += data,
tup += target,
dataset.append(tup)
#print(dataset)

currentModel = None

for X, y in dataset:
    #X = StandardScaler().fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3)
    clf.fit(X_train, y_train)
    predictions = clf.predict(X_test)
    score = clf.score(X_test, y_test)
    currentModel = clf
    # print("x_test")
    # print(X_test)
    # print("y_test")
    # print(y_test)

    feature = [5.9, 3, 5.1, 1.8]
    #feature = StandardScaler().transform(feature)
    print(clf.predict(feature))
    print(score)


feature2= [5.9, 3, 5.1, 1.8]


#print(currentModel.predict(feature2))


f = open("/Users/yilu/Projects/mysql-server/python/output.txt","w")

modelDump = pickle.dumps(currentModel)


#read from table and do prediction


f.write("%s\r" % modelDump)

f.close()

f = open("/Users/yilu/Projects/mysql-server/python/output.txt","r")
modelDumpDes = f.read()
f.close()




# model2 = pickle.loads(modelDumpDes)
# print("print deserilized model")
# print(model2.predict(feature2))

# dropIfExistQuery = "DROP TABLE IF EXISTS " + tableName + ";"
# ExecQuery(dbConnection, dropIfExistQuery)
#
# createTableQuery = "CREATE TABLE " + tableName + " (target varchar(255), score double);"
# ExecQuery(dbConnection, createTableQuery)
#
# ## insert into temp table with feature and score
# insertResultQuery = "INSERT INTO " + tableName + " VALUES ('" + str(clf.predict(feature)[0]) + "', " + str(score) + ");"
# ExecQuery(dbConnection, insertResultQuery)

# select query command
#selectResutlQuery = "select * from " + tableName

#print(selectResutlQuery)

dbConnection.close()