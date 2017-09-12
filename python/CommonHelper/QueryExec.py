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

def GetClusteringTable(selectQuery) :
    conn = pymysql.connect(host=hostname, user=username, passwd=password, db=database)
    cur = conn.cursor()
    cur.execute(selectQuery)
    data = []
    for row in cur:
        dataR = []
        for r in row:
            dataR.append(r)

        data.append(dataR)
    data = np.array(data)
    return data

def CreateOutput(predict, score):
    conn = pymysql.connect(host=hostname, user=username, passwd=password, db=database)

    id = "out" + str(uuid.uuid4()).replace('-', '0')
    createOutTableIfNotExistsQuery = "CREATE TABLE IF NOT EXISTS predictions (id varchar(255), predict varchar(255), score double);"
    CommitQuery(createOutTableIfNotExistsQuery, conn)

    insertIntoQuery = "INSERT INTO predictions VALUES ('" + id + "', '" + str(predict[0]) + "', " + str(score) + ");"
    CommitQuery(insertIntoQuery, conn)

    selectResutlQuery = "select predict, score from predictions where id = '" + id + "'"

    conn.close()

    print(selectResutlQuery)

def CreateClusterOutput(select_queries, max_number):
    conn = pymysql.connect(host=hostname, user=username, passwd=password, db=database)

    id = "cls" + str(uuid.uuid4()).replace('-', '0')

    # Drop the cluster table if exists (avoid creating many temp table for clustering)
    dropTableIfExistsQuery = "DROP TABLE IF EXISTS " + str(id) + ";"
    CommitQuery(dropTableIfExistsQuery, conn)

    # make the query union together and limit max_number

    # select into clustering_result table
    selectSimilarIntoTableQuery = "CREATE TABLE " + str(id) + " (" + select_queries[0] + ");"
    CommitQuery(selectSimilarIntoTableQuery, conn)

    # if there is more than just one query, insert into table with select limit to max number


    # select the result back
    selectResutlQuery = "select * from " + str(id) + ";"

    conn.close()

    print(selectResutlQuery)

def CommitQuery(query, conn):
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()