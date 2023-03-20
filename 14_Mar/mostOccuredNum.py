def mostOccured(x):
    counter = 0
    result = x[0]
    for i in x:
        curr_frequency = x.count(i)/////////////////
        if(curr_frequency> counter):
            counter = curr_frequency
            result = i
            return result
def getCount(): 
    x=input("Enter the letter to find most occurence : ")       
    y=mostOccured(x)
    print(y)

getCount()