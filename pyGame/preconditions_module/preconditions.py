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
    conditionName = 'Defult'
    conditionCode = 'False'
    failMessage = 'Defult Never Works'
    params = []

def runPrecondition(state, conditionName, parameters):
    condition = preconditions[conditionName]
    index = 0
    pars = {}
    for key in condition.params:
        if(isinstance(parameters[index], str)):
            param = "'" + parameters[index] + "'"
        else:
           param = str(parameters[index])
        aLine = key + ' = ' + param
        exec(aLine)
        index=index+1
    comand = 'result = ' + condition.conditionCode
    exec(comand)
    aResult = locals()['result']
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
