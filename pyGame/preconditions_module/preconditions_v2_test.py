import preconditions_v2
import t7_pyhop_v1
#testing for preconditions_v2_v2
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

def isOnFunction(state, factor1, factor2, test1, test2):
    return (factor1 > factor2) and test2 and state.dic['test']

isOn = preconditions_v2.Precondition()
isOn.conditionName = 'condition one'
isOn.conditionFunction = isOnFunction
isOn.failMessage = 'factor1 wasnt greater than factor2'

preconditions_v2.addToPreconditions(isOn)
params = [2, 3, 'test', True]
result = preconditions_v2.runPrecondition(state1, 'condition one', params)
print(result)

def canMove(state, name, goal):
    return state.dic['can move'][name] == True

canMoveCondition = preconditions_v2.Precondition()
canMoveCondition.conditionName = 'can move'
canMoveCondition.conditionFunction = canMove
canMoveCondition.failMessage = "cant move"

preconditions_v2.addToPreconditions(canMoveCondition)

def move(state, name, goal):
    newLocation = goal.dic['locations'][name]
    state.dic['locations'][name] = newLocation

preconditions_v2.addPreconditionsToTask('move',['can move'])

def runMove(state, pars):
    r = preconditions_v2.runPreconditions(state, 'move', pars)
    if r != True:
        print(r)
    else:
        move(state, *pars)
        print('moved')

runMove(state1, ['a', goal1])

state1.dic['can move']['a'] = True
runMove(state1, ['a', goal1])

input('press any key to end')
