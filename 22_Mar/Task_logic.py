from Task_db import isPresent,insertVaribleIntoTable,updateSqliteTable,popTask,getTaskInfo

def present(id):
    pre=isPresent(id)

def addTask(x):
    pre=insertVaribleIntoTable(x)
    return pre
    
def updateTask(x):
    pre = updateSqliteTable(x)
    return pre
    
def viewTask(id):
    pre = getTaskInfo(id)
    return pre

def removeTask(id):
    pre=popTask(id)
    return pre


    
