from logic import addWord,viewWord,allWord,occurWord
def start():
    exit=False

    while not exit:
        print("1. add word\n2. view word\n3. view words based on occurences\n4. view all words howmany occorence\n0. exit")
        ch=int(input("Enter u r choice: "))

        if ch==0:
            exit=True

        elif ch==1:
            name = input("Enter employee's name: ")
            res=addWord(name)
            print(res,"\n")
               
        elif ch==2:
            res=viewWord()
            print(res,"\n")

        elif ch==3:
            inte=int(input("Enter the occurence to see the names: "))
            res=occurWord(inte)
            print(res,"\n")

        elif ch==4:
            res=allWord()
            print(res,"\n")
            
        
              