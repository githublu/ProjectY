import pymysql
import numpy as np
import uuid

hostname = 'localhost'
username = 'root'
password = ''
database = 'testdb1'

# # Simple routine to run a query on a database and print the results:
def ExecQuery(query) :
    conn = pymysql.connect(host=hostname, user=username, passwd=password, db=database)
    result = []
    cur = conn.cursor()
    cur.execute(query)
    for row in cur:
        result.append(row)

    conn.close()
    return result

def GetTable(selectQuery) :
    conn = pymysql.connect(host=hostname, user=username, passwd=password, db=database)
    cur = conn.cursor()
    cur.execute(selectQuery)
    data = []
    target = []
    dataset = []
    tup = ()
    for row in cur:
        targetR = row[len(row) - 1]
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
    return dataset

def CreateOutput(predict, score):
    id = "out" + str(uuid.uuid4()).replace('-', '0')
    createOutTableIfNotExistsQuery = "CREATE TABLE IF NOT EXISTS predictions (id varchar(50), predict varchar(255), score double);"
    ExecQuery(createOutTableIfNotExistsQuery)
    insertIntoQuery = "INSERT INTO predictions VALUES ('" + id + "', '" + str(predict) + "', " + str(score) + ");"
    ExecQuery(insertIntoQuery)
    selectResutlQuery = "select * from predictions where id = '" + id + "';"
    print(selectResutlQuery)
