regNum =1
nameList=[]
usnList=[]
def add():
    global regNum
    a = "1BY24CS"
    while True:
        name=input("Enter the name of Student")
        if name == "":
            break
        nameList.append(name)      
        usnList.append(a+str(regNum))
        regNum=regNum+1
        if regNum == 71:
           print("Class is pack")
           break
        
def view():
    for i in range(len(nameList)):
        print(nameList[i])
        print(usnList[i])
        print("-----------------------------")

def disname():
    b=input("enter the usn")
    if b in usnList:
        c=usnList.index(b)
        print(nameList[c])
    else:
       print("Enter properly")

def find():
    print(regNum-1)

def mainmethod():
    while True:
       print("Enter 'a' to add,'v' to view std. details,'f' to find class strength','d to display the name of students','e' to exit the program")
       choose=input("Enter your choice")
       if choose == 'a':
           add()
       elif choose == 'v':
           view()
       elif choose == 'f':
           find()
       elif choose=='d':
           disname()
       elif choose=="e":
           break 
       else:
           print("Enter properly")
mainmethod()

