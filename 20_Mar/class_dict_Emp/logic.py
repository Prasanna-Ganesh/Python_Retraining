from emp import emp
from empStatuscode import EmployeeStatusCode
e1=emp(1,"prasanna",10000,"GT",21)
e2=emp(2,"akash",12000,"tech",25)
e3=emp(3,"jithu",20000,"admin",23)
e4=emp(4,"kisoo",10000,"analyst",21)
e5=emp(5,"deepak",200000,"governance",25)

d={e1.empno:e1,e2.empno:e2,e3.empno:e3,e4.empno:e4,e5.empno:e5}
def empDetails(n):
    try:
        return d[n]
    except:
        return "No such ID"
    
def deptEmployees(n):
    l=[]
    for i in d.values():
        if i.empdeptno==n:
            l.append(i.empname)
    return l

def ispresent(n):
    if d.get(n) is not None:
        return EmployeeStatusCode(1,"got result",d[n])
    else:
        return EmployeeStatusCode(0,"no result",None)