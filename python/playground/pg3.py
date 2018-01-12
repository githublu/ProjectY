import pymysql
import numpy as np
import uuid

hostname = 'localhost'
username = 'root'
password = ''
database = 'testdb1'

conn = pymysql.connect(host=hostname, user=username, passwd=password, db=database)
cur = conn.cursor()
cur.execute("SELECT COUNT(*) FROM iris")

#print(cur)

for row in cur:
    print(row)

conn.close()