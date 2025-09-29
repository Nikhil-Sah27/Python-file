names = "Nikhil,Sah"
print(names[0:7])

print(len(names))

a = "Nikhil"
print("Nikhil has a " , len(a) , "letter.\n")

print(a[1:4]) #including 1 but not 4
print(a[:4])
print(a[1:-3]) #or print(a[1:len(a)-3])
print(a[1:len(a)-3]) # 3rd(n-1) will be ignored
print(a[len(a)-1:len(a)-3]) #prints no thing as it range form 5:3
print(a[len(a)-3:len(a)-1])

nm = "Harry"
print(nm[-4:-2])
