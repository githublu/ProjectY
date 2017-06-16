import datetime
import sys

f = open("/Users/yilu/Projects/mysql-server/python/output.txt","a")
f.write("%s\r" % datetime.datetime.now())
f.write("%s\r" % str(sys.argv))

# scrub the first predic keyword
rawQuery = sys.argv[1]
startQuery = rawQuery[8: ]

# select * from t1 where 

print(startQuery)
f.close()
