def swap(a,b):
    temp=a
    a=b
    b=temp
    return a,b

def run():
    a=input("Enter a:")
    b=input("Enter b:")
    c,d=swap(a,b)
    print("{} After swapping : {}".format(a,c))
    print("{} After swapping : {}".format(b,d))
run()
