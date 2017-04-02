from __future__ import print_function
import block_world_operators_2
import blocks_world_methods2
import blocks_world_methods
from pyhop_module.pyhop import *
#from preconditions_module.t7_pyhop_v1 import *
from validation_module.validator import *
from model.plan_tree import *
from parse_module.parser import *

#
#print('')
#print_operators()

#print('')
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

#Plan
#action = [('move_blocks', goal_state)];
#print(action)


# [('unstack', 'a', 'b'), ('putdown', 'a'), ('pickup', 'b'), ('stack', 'b', 'a'), ('pickup', 'c'), ('stack', 'c', 'b')]
# ['unstack', 'pickup', 'putdown', 'stack']
# Plan

test_tree = Plan_Tree()
test_tree.add_task(('unstack', 'a', 'b'))
test_tree.add_task(('putdown', 'a'), test_tree.root)
test_tree.add_task(('pickup', 'b'), test_tree.nodes[2])
test_tree.add_task(('stack', 'b', 'a'), test_tree.nodes[3])
print('')
print("-----Display the tree-----")
test_tree.display_all()

node = test_tree.get_node(4)
plan = test_tree.get_plan(node)
#for task in plan:
#    print('Task: ' + ', '.join(task))

#Integrating plan_tree with validator testing
print('')
print('')
print("------Integrating plan_tree with validator testing---------")
test_validator = Validator(state1,goal_state,test_tree)
#pyhop(state1,action,verbose=1)
print("------THIS IS THE PLAN Generated From the PLAN TREE--------")
plan = test_validator.run_pyhop(node)
print('')
print("------This is the plan generated from pyhop after running the user plan-------")
print(plan)
print('')

tasks = test_validator.get_tasks()
print(tasks)
print('')
print("Testing File Read and Write")
parser = Parser()
parser.file_path ="C:\\Users\Bnol\Documents\pyhop_files"
parser.dump_to_file(test_validator, "demo.json")

validator_copy = parser.read_file("demo.json")

plan2 = validator_copy.run_pyhop(node)
print('')
print("------This is the plan generated from the copy read back in from the json file------")
print(plan2)
#Print test state
#print_state(state1)
