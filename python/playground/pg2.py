userquery = "select sepal_length, sepal_width, petal_length, petal_width from iris;"
index_of_from = userquery.find("from")
print index_of_from
print userquery.find(" ", index_of_from+4)
#all_params = userquery[6: index_of_from].split(",")

table_name = userquery[index_of_from+5:userquery.find(" ", index_of_from+5)]
print table_name
