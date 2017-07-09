import pymysql
import numpy as np

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