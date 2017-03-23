import datetime

preconditions = {}

preconditionsForTasks = {}

failLog = []
def addPreconditionsToTask(taskName, preconditions):
    preconditionsForTasks[taskName] = preconditions

def addToPreconditions(condition):
    preconditions[condition.conditionName] = condition

def getPreCondition(name):
    return preconditions[name]

class Precondition:
    def defultFunction():
        return False
    conditionName = 'Defult'
    conditionFunction = defultFunction
    failMessage = 'Defult Never Works'

def runPrecondition(state, conditionName, parameters):
    condition = preconditions[conditionName]
    index = 0
    pars = {}
    
    aResult = condition.conditionFunction(state, *parameters)
    toReturn = True
    if(aResult == False):
        toReturn = condition.failMessage
    return toReturn

def runPreconditions(state, task, parameters):
    success = True
    if task in preconditionsForTasks:
        conditions = preconditionsForTasks[task]
        index = 0
    
        while (index < len(conditions)) and success == True:
            success = runPrecondition(state, conditions[index], parameters)
            index = index +1
    return success

def addFailure(message, report):
    failLog.append({'message':message, 'report':report, 'time': datetime.datetime.now()})
