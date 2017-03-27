from __future__ import print_function

from validation_module.validator import *

#
print('')
print_operators()

print('')
print_methods()

#Inital State
state1 = State('state1')
state1.pos={'a':'b', 'b':'table', 'c':'table'}
state1.clear={'c':True, 'b':False,'a':True}
state1.holding=False

#Goal State
goal_state = Goal('goal1a')
goal_state.pos={'c':'b', 'b':'a', 'a':'table'}
goal_state.clear={'c':True, 'b':False, 'a':False}
goal_state.holding=False

#Plan
action = [('move_blocks', goal_state)];
#print(action)
test_validator = Validator(state1,goal_state,action)
#pyhop(state1,action,verbose=1)
plan = test_validator.run_pyhop()
print("------THIS IS THE PLAN--------")
print(plan)
tasks = test_validator.get_tasks()
print(tasks)
#Print test state
#print_state(state1)
