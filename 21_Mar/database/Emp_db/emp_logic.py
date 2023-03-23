# from emp_model import EmployeeStatusCode,emp
# e1=emp(1,"prasanna",10000,"GT",21)
# e2=emp(2,"akash",12000,"tech",25)
# e3=emp(3,"jithu",20000,"admin",23)
# e4=emp(4,"kisoo",10000,"analyst",21)
# e5=emp(5,"deepak",200000,"governance",25)

# d={e1.empno:e1,e2.empno:e2,e3.empno:e3,e4.empno:e4,e5.empno:e5}
from emp_model import emp
from emp_db import insertVaribleIntoTable,getDeptInfo,getEmployeeInfo

e1=emp(21,"prasanna",10000,"GT",21)
e2=emp(22,"akash",12000,"tech",25)
e3=emp(23,"jithu",20000,"admin",23)
e4=emp(24,"kisoo",10000,"analyst",21)
e5=emp(25,"deepak",200000,"governance",25)
i1=insertVaribleIntoTable(e1)
i2=insertVaribleIntoTable(e2)
i3=insertVaribleIntoTable(e3)
i4=insertVaribleIntoTable(e4)
i5=insertVaribleIntoTable(e5)

def empDetails(n):
    empdetail=getEmployeeInfo(n)
    return empdetail

def deptEmployees(n):
    dept=getDeptInfo(n)
    return dept

    


# from db import getEmployeeInfo, insertemployee, getDeptInfo
# def insertEmp(info):
#     insertemployee(info)
# def viewEmp(num):
#     emp = getEmployeeInfo(num)
#     return emp
# def viewDept(num):
#     dept = getDeptInfo(num)
#     return dept