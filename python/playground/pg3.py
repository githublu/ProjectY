from ClusteringStateMachine import *
import numpy as np
userquery = "select sepal_length, sepal_width, petal_length, petal_width from iris;"
output = np.asarray(ClusteringStateMachineStart("select sepal_length, sepal_width, petal_length, petal_width from iris;", [5.9, 3, 5.1, 1.8], 2))




# query = "SELECT * FROM "
#
# # get a list of parameters
# index_of_from = userquery.find("from")
# all_params = userquery[6: index_of_from].split(",")
# table_name = userquery[index_of_from+5:userquery.find(" ", index_of_from+5)]
# is_first = True
# query += table_name + " WHERE "
# for i in range(0, len(all_params)):
#     if is_first:
#         query += str(all_params[i]) + " = " + str(output[0][i])
#         is_first = False
#     else:
#         query += " AND " + str(all_params[i]) + " = " + str(output[0][i])


print output