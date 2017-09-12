import sys
from Logger import *
from ManagementOperationStateMachine import *

#EntryPoint("select sepal_length, sepal_width, petal_length, petal_width from iris;", [5.9, 3, 5.1], "SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS where table_name = 'iris' and TABLE_SCHEMA = 'testdb1'", "petal_width")
#EntryPoint(select_statement, )

if is_debug():
    # make debug change in state machine
    Start(1, 2, 3, 4)
else:
    select_statement = sys.argv[1]
    predict_input = sys.argv[2].split(',')
    schema_statement = sys.argv[3]
    target_name = sys.argv[4]
    Start(select_statement, predict_input, schema_statement, target_name)
