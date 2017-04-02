#from preconditions_module.t7_pyhop_v1 import *
from pyhop_module.pyhop import *

class Validator:
    """Interfaces with pyhop to validate a user plan"""

    # Variables created that user needs to define
    # initial_state and goal_state will follow the same structure for input and output
    # if a dictionary exists in initial state it should also exist in final state, however the contents may be different
    initial_state = {}
    goal_state = {}
    # Format structure for plans looks like this per plan [('method',operator_key,operator_key.,,,)]
    user_plan = None
    pyhop_plans = {}

    def __init__(self, initial_state, goal_state, user_plan):
        """Initializes Validator object with the provided values

        :param State initial_state: the initial state, on which the plan operates
        :param State goal_state: the state which is to be achieved
        :param str user_plan: user constructed plan that is to be validated
        """
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.user_plan = user_plan
        self.pyhop_plan = ""

    # this is the method called to execute pyhop and returns the plan, BOOYAH!!
    def run_pyhop(self,node):
        """Produces and returns a plan using pyhop"""
        # print(self.user_plan)
        # print(self.initial_state)
        if self.user_plan is not None:
            plan = self.user_plan.get_plan(node)
           # print("print out of the plan")
            print(plan)
            pyhop_object = pyhop(self.initial_state, plan, verbose=0)
            self.pyhop_plan = pyhop_object
            return pyhop_object
        return "Fail"
    #Get all tasks from pyhop
    #@return - list of tasks
    def get_tasks(self):
        """Returns a list of operators"""
        tasks = get_operators()
        return tasks
