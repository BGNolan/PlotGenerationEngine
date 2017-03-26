
from __future__ import print_function
from pyhop_module.blocks_world_operators import *
from pyhop_module.blocks_world_methods import *
from pyhop_module.blocks_world_methods2 import *
from pyhop_module.pyhop import *
from validation_module.validator import *
from parse_module.parser import *
#
print('')
print_operators()

print('')
print_methods()

# Initial State
state1 = State('state1')
state1.pos={'a':'b', 'b':'table', 'c':'table'}
state1.clear={'c':True, 'b':False,'a':True}
state1.holding=False

# Goal State
goal_state = Goal('goal1a')                     # Is this supposed to be a state instead of a goal object?
goal_state.pos = {'c': 'b', 'b': 'a', 'a': 'table'}
goal_state.clear = {'c': True, 'b': False, 'a': False}
goal_state.holding = False

# Plan
action = [('move_blocks', goal_state)]
# print(action)
test_validator = Validator(state1, goal_state, action)
# pyhop(state1,action,verbose=1)
plan = test_validator.run_pyhop()
print("------THIS IS THE PLAN--------")
print(plan)
# test get_tasks()
tasks = test_validator.get_tasks()
print("------THESE ARE THE TASKS--------")
print(tasks)

# test saving/loading
print("----TEST SAVING AND LOADING----")
parser = Parser()
parser.file_path = "C:\Users\Ryan\Downloads\PlotGenerationEngine-master\pyGame\parse_module"
parser.dump_to_file(test_validator, "plan.json")
val_copy = parser.read_file("plan.json")
print(val_copy.pyhop_plan)  # The "u" before each string, it just indicates encoding
print("Element[0][0] of copy: " + val_copy.pyhop_plan[0][0])
