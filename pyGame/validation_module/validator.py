from pyhop_module.pyhop import *




class Validator():
    # Variables crateed that user needs to define
    # inital_state and goal_state will follow the same strucutre for input and ouput
    # if a dictionary exists in inital state it should also exist in final state however the contents may be different
    initial_state = {}
    goal_state = {}
    # Formate structure for plans looks like this per plan [('method',operator_key,operator_key.,,,)]
    user_plan = {}
    pyhop_plans = {}



    # contrusctor
    def __init__(self, inital_state, goal_state, user_plan):
        self.initial_state = inital_state
        self.goal_state = goal_state
        self.user_plan = user_plan
        self.pyhop_plan= ""


    # this is the method called to execute pyhop and returns the plan, BOOYAH!!
    def run_pyhop(self):
        #print(self.user_plan)
        #print(self.initial_state)
        pyhop_object = pyhop(self.initial_state, self.user_plan,verbose=1)
        self.pyhop_plan = pyhop_object
        return pyhop_object

    #Get all tasks from pyhop
    #@return - list of tasks
    def get_tasks(self):
        tasks = get_operators()
        return tasks.keys()
