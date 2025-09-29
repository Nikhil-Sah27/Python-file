num=input("Enter a multidigit number")
dict={}
for i in num:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)