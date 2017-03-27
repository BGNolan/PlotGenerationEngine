import preconditions
import t7_pyhop_v1
#testing for preconditions
state1 = t7_pyhop_v1.State('state1')
state1.dic = {}
state1.dic['test']=True

state1.dic['locations'] = {}
state1.dic['locations']['a'] = 'dayton'
state1.dic['can move'] = {}
state1.dic['can move']['a'] = False

goal1 = t7_pyhop_v1.Goal('goal1')
goal1.dic = {}
goal1.dic['locations'] = {}
goal1.dic['locations']['a']='home'


isOn = preconditions.Precondition()
isOn.conditionName = 'condition one'
isOn.params = ['factor1', 'factor2', 'test1', 'test2']
isOn.conditionCode = '(factor1 > factor2) and test2 and state.dic[\'test\']'
isOn.failMessage = 'factor1 wasnt greater than factor2'

preconditions.addToPreconditions(isOn)
params = [2, 3, 'test', True]
result = preconditions.runPrecondition(state1, 'condition one', params)
print(result)

canMoveCondition = preconditions.Precondition()
canMoveCondition.conditionName = 'can move'
canMoveCondition.params = ['name']
canMoveCondition.conditionCode = "state.dic['can move'][name] == True"
canMoveCondition.failMessage = "cant move"

preconditions.addToPreconditions(canMoveCondition)

def move(state, name, goal):
    newLocation = goal.dic['locations'][name]
    state.dic['locations'][name] = newLocation

preconditions.addPreconditionsToTask('move',['can move'])

def runMove(state, pars):
    r = preconditions.runPreconditions(state, 'move', pars)
    if r != True:
        print(r)
    else:
        move(state, *pars)
        print('moved')

runMove(state1, ['a', goal1])

state1.dic['can move']['a'] = True
runMove(state1, ['a', goal1])

input('press any key to end')

""" 
summary
user makes preconditions
user assossiates 7_pyhop_v1 methods with preconditions
add funconality to phyop that uses preconditions


How to uses this?

user task:
User must create a condition by providing there own:
    condition name
    python boolean equation (as a string)
    varable names (as array of string) (these names are used in the bool equation)
        see Params
    fail message (as a string)
User then assossiates preconditions with 7_pyhop_v1 methods, this is done by
    adding custom conditions to conditions list (see line 36)
    adding relationship between 7_pyhop_v1 method name, and list of conditidion names (see line 42)

when done corectly user dosn't need to return false in 7_pyhop_v1 methods, 7_pyhop_v1 will fail if preconditons not valid.
    if method still returns false, it means users preconditions don't take all fail states in mind

modifications to 7_pyhop_v1 needed
    in seek_plan: 
        before method is run, but after we check method is in 7_pyhop_v1:
            run check preconditions for that method
                7_pyhop_v1 passes method name, uses this name when run checkPreconditions
                7_pyhop_v1 passes parameters as array, uses this for checkpreconditions

Params*:
    how do the parameters in varables get there values?
    the params get there values from the method they are assossiated with
    example: method(state, par1, par2, pare3, goal)
    when you want to uses methodin 7_pyhop_v1 you need to call: 7_pyhop_v1(state, [('method name', par1, par2,...,parn)] )
    say we assossiate method with precondition con1
    con1 has pars ['p1', 'p2', 'p3']
    when 7_pyhop_v1 is run the paramters used for that are also used to give values to preconditions
    so p1 = par1
    in 7_pyhop_v1 the first paramter for a method when defined is always state, we ignore this.
    runPrecondition has a state by defult, see state*
    your pars for precondition dosn't need to inclued ALL pars for the method, and shoudn't inclued state
        (ex method move, lines 32 and 38)

State
    preconditions have a parameter state by defult
    7_pyhop_v1 methods all have a state as a paramter, this prameter is ignored in Params, see params*
    so users shouldn't inclued a state par, and shoudn't create a par called 'state'

"""