from logic import fillList,viewList,change,delete,asc,dec,occur
def start():
    exit=False
    while not exit:
        print("0. exit\n1. Fill up the list with 10 numbers\n2. view list\n3. change num\n4. del num\n5.ascending order list\n6. Decending order list")
        ch= int(input("Enter u r choice : "))
        if ch==0:
            exit=True
        elif ch==1:
           fillList()
           print("10 Random number filled with list")
        
        elif ch==2:
            res=viewList()
            print(res)
        
        elif ch==3:
            a=int(input("Enter the num to change: "))
            b=int(input("Enter the new number to replace: "))
            res=change(a,b)
            print(res)

        elif ch==4:
            ele=int(input("Enter the num to remove: "))
            res=delete(ele)
            print(res)

        elif ch==5:
            res=asc()
            print(res)

        elif ch==6:
            res=dec()
            print(res)

        elif ch==7:
            res =occur()
            print(res)




