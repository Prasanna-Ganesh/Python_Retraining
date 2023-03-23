class emp():
 
    def __init__(self,empno,empname,empsalary,empdesignation,empdeptno):
        self.empno=empno
        self.empname=empname
        self.empsalary=empsalary
        self.empdesignation=empdesignation
        self.empdeptno=empdeptno
        
    def __repr__(self):
        return f"Employee No:{self.empno},\nname:{self.empname},\ndept_id:{self.empdeptno},\nsalary:{self.empsalary},\nDesignation:{self.empdesignation}"
        

class EmployeeStatusCode():
    def __init__(self,statuscode,message,empobj):
        self.statuscode=statuscode
        self.message=message
        self.empobj=empobj

    def __repr__(self):
        return f"{self.statuscode},{self.message},{self.empobj}"

