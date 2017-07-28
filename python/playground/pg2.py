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
import pymysql

hostname = 'localhost'
username = 'root'
password = ''
database = 'testdb1'

# # Simple routine to run a query on a database and print the results:
def doQuery( conn, record) :
    cur = conn.cursor()
    query = "INSERT INTO iris VALUES (%s, %s, %s, %s, '%s')" % (record[0], record[1], record[2], record[3],record[4])
    print(query)
    cur.execute(query)
    conn.commit()

myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )


iris = datasets.load_iris()
irisData = iris.data
irisTarget = iris.target
rows = irisData.shape[0]
cols = irisData.shape[1]

#print(irisData.shape)

#indextToTarget = [0: 'setosa', 1: 'versicolor', 2: 'virginica']
#'setosa', 'versicolor', 'virginica'


#print(iris.target_names[0])

# for x in range(0, rows):
#     record = np.append(irisData[x,:],iris.target_names[irisTarget[x]])
#     print(record)
#     doQuery( myConnection, record)

myConnection.close()