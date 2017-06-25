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

hostname = 'localhost'
username = 'root'
password = ''
database = 'testdb1'

# # Simple routine to run a query on a database and print the results:
def ExecQuery( conn, query) :
    cur = conn.cursor()
    # query = "INSERT INTO iris VALUES (%s, %s, %s, %s, '%s')" % (record[0], record[1], record[2], record[3],record[4])
    # print query
    cur.execute(query)
    conn.commit()


datasets = [make_moons(noise=0.3, random_state=0)]
#irisDatasets = datasets.load_iris()

#print(irisDatasets.data)
# sample = []
# tup = ()
# data = np.array(irisDatasets.data)
# target = np.array(irisDatasets.target)
# tup += data,
# tup += target,
# sample.append(tup)

#print(sample)
#print(irisDatasets.target_names)

clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)


for X, y in datasets:
	X = StandardScaler().fit_transform(X)
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.2)
	
clf.fit(X_train, y_train)
score = clf.score(X_test, y_test)
feature = np.array([ 2.11509784, -0.04624397]).reshape(1, -1)
# print(clf.predict(feature)[0])
# print(score)

dbConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )

## create temp table with feature and score
tableName = str(uuid.uuid4()).replace('-', '0')

dropIfExistQuery = "DROP TABLE IF EXISTS " + tableName + ";"
ExecQuery(dbConnection, dropIfExistQuery)

createTableQuery = "CREATE TABLE " + tableName + " (target varchar(255), score double);"
ExecQuery(dbConnection, createTableQuery)

## insert into temp table with feature and score
insertResultQuery = "INSERT INTO " + tableName + " VALUES ('" + str(clf.predict(feature)[0]) + "', " + str(score) + ");"
ExecQuery(dbConnection, insertResultQuery)

# select query command
selectResutlQuery = "select * from " + tableName

print(selectResutlQuery)

dbConnection.close()




