import random
list1=[]

def fillList():
    list1.clear()
    for i in range(0,10):
        list1.append(random.randint(0,100))
    return list1
    
def viewList():
    return list1

def change(a,b):
    if a not in list1:
        return "The num not in the list"
    elif b in list1:
        return "The num already in list"
    else:
        i = list1.index(a)
        list1[i] = b
        return "number has changed"
    
def delete(ele):
    if ele in list1:
        list1.remove(ele)
        return "Number removed"
    else: 
        return "num not found"
    
def asc():
    asc=list1.copy()
    asc.sort()
    return asc

def dec():
    dec=list1.copy()
    dec.sort(reverse=True)
    return dec

def occur():
    a=[]
    b=[]
    count=0
    for i in list1:
        c=list1.count(i)
        count=c
        a.append(i)
        b.append(count)
        d=dict(zip(a,b))
        return d





