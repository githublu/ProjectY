import pickle as pickle


def CacheModel(user_query, model):
    #TODO: convert user_query into hash that can be easily searched

    f = open("/Users/yilu/Projects/mysql-server/python/output.txt","w")
    f.write("%s\r" % pickle.dumps(model))
    f.close()

def GetCachedModel(user_query):
    return False
    #
    # if file_exit:
    #     f = open("/Users/yilu/Projects/mysql-server/python/output.txt","r")
    #     modelDumpDes = f.read()
    #     f.close()
    #     return modelDumpDes
    # else:
    #     return False