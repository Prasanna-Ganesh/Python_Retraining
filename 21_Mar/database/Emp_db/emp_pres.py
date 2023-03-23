from emp_logic import empDetails,deptEmployees
def start():
    exit=False
    while not exit:
        print("0. Exit\n1. Enter emp no to view emp details\n2. Enter dept id to view details of emp\n3. Status check")
        ch=int(input("Enter u r Choice: "))
        if ch==0:
            exit=True

        elif ch==1:
            n=int(input("Enter Employee id to view details: "))
            res=empDetails(n)
            print(res,"\n")

        elif ch==2:
            n=int(input("Enter the dept id to view the employees: "))
            res=deptEmployees(n)
            print(res,"\n")

        # elif ch==3:
        #     num = int(input("Enter employee no:"))
        #     p = ispresent(num)
        #     print(p,"\n")


        
            


