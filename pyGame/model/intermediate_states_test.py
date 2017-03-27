
from __future__ import print_function
from model.blocks_world_operators import *
from model.blocks_world_methods import *
from model.blocks_world_methods2 import *
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
goal_state = Goal('goal1a')
goal_state.pos = {'c': 'b', 'b': 'a', 'a': 'table'}
goal_state.clear = {'c': True, 'b': False, 'a': False}
goal_state.holding = False

# Plan
action = [('move_blocks', goal_state)]
test_validator = Validator(state1, goal_state, action)
plan = test_validator.run_pyhop()
print("------THIS IS THE PLAN--------")
print(plan)

# Intermediate states
print("------THESE ARE THE POSITIONS IN THE INTERMEDIATE STATES--------")
states = test_validator.get_states_list()
for i in range(1, len(states)):
    print(states[i].pos)
print("----------------------------------------------------------------")
print("Pre state for last task ")
print(test_validator.get_pre_state().pos)
print("Post state for last task ")
print(test_validator.get_post_state().pos)