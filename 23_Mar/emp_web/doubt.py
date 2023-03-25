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
print(jsonlist)


def ispresent(n):
    if e1.get(n) is not None:
        return EmployeeStatusCode(1, "got result", e1)
    else:
        return EmployeeStatusCode(0, "no result", None)
res=ispresent(75)
print(res)