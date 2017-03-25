#This file is used for testing the functionality of the model
from __future__ import print_function
from pyhop_module.blocks_world_operators import *
from pyhop_module.blocks_world_methods import *
from pyhop_module.blocks_world_methods2 import *
from pyhop_module.pyhop import *
from validation_module.validator import *
from plan_tree import *
#
print('')
#print_operators()

print('')
#print_methods()

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
# [('unstack', 'a', 'b'), ('putdown', 'a'), ('pickup', 'b'), ('stack', 'b', 'a'), ('pickup', 'c'), ('stack', 'c', 'b')]
#['unstack', 'pickup', 'putdown', 'stack']
#Plan
action = [('move_blocks', goal_state)];

test_tree = Plan_Tree()
test_tree.add_task(('unstack', 'a', 'b'))
test_tree.add_task(('putdown', 'a'),test_tree.root)
test_tree.add_task(('pickup', 'b'),test_tree.root)
test_tree.add_task(('stack', 'b', 'a'),test_tree.nodes[2])
test_tree.display_all()