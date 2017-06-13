import datetime
f = open("/Users/yilu/Projects/mysql-server/python/output.txt","a")
f.write("%s\r" % datetime.datetime.now())
f.close()
