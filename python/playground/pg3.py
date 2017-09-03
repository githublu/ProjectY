from ClusteringStateMachine import *

output = Start("select sepal_length, sepal_width, petal_length, petal_width from iris;", [5.9, 3, 5.1, 1.8], 2)
print output