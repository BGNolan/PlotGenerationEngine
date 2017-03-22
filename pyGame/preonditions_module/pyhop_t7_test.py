import t7_pyhop_v1
import preconditions

canMoveCondition = preconditions.Precondition()
canMoveCondition.conditionName = 'can move'
canMoveCondition.params = ['name']
canMoveCondition.conditionCode = "state.dic['can move'][name] == True"
canMoveCondition.failMessage = "cant move"

preconditions.addToPreconditions(canMoveCondition)

def move(state, name, goal):
    newLocation = goal.dic['locations'][name]
    state.dic['locations'][name] = newLocation
    return[]
t7_pyhop_v1.declare_methods('move',move)
preconditions.addPreconditionsToTask('move',['can move'])

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

t7_pyhop_v1.pyhop(state1,[('move','a',goal1)], verbose=2)

for failure in preconditions.failLog:
    print(failure['message'])

input('press any key to end')
