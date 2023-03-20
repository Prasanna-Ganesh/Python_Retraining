
def addAll(l1):
    count=0
    for i in range(0,len(l1)):
        count=l1[i]+count
    return count


def sumofAllNum():
    l1=[10,20,30]
    l2=addAll(l1)
    print("the sum of list is ", l2)
    

sumofAllNum()