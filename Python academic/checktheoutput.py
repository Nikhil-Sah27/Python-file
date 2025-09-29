cse=list()
while (True):
    n = input("Enter")
    if(int(n[0])%3):
        cse.append(int(n[0]))
        cse.append(len(n))
    if (n=='10'):
        break
    print("list=",cse)
print("Sum=",sum(cse))


