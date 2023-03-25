from emp_model_web import emp,EmployeeStatusCode
import json
e1 = emp(21, "prasanna", 10000, "GT", 21)
e2 = emp(22, "akash", 12000, "tech", 25)
e3 = emp(23, "jithu", 20000, "CEO", 23)
e4 = emp(24, "kisoo", 10000, "analyst", 21)
e5 = emp(25, "Tinu", 200000, "Director", 25)
# print(json.dumps(e1.__dict__))

listofemp=[e1,e2,e3,e4,e5]
jsonlist=json.dumps([x.__dict__ for x in listofemp])



def empDetails(n):
    try:
        return d[n]
    except:
        return "No such ID"


def deptEmployees(n):
    l = []
    for i in d.values():
        if i.empdeptno == n:
            l.append(i.empname)
    return l


def ispresent(n):
    if jsonlist.get(n) is not None:
        return EmployeeStatusCode(1, "got result", jsonlist[n])
    else:
        return EmployeeStatusCode(0, "no result", None)


