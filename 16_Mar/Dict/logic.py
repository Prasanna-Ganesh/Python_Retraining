employees = {}

def addWord(name):
    if name in employees.keys():
        employees[name] = employees[name]+1
        return"Name already present, Count added"
        
    else:
        employees[name] = 1
        return "Name Added"
    

def viewWord():
    return employees.get(keys)

def allWord():
    return employees

def occurWord(inte):
    d1=[]
    for emp in employees:
        if employees[emp]>=inte:
            d1.append(emp)
    return d1
    