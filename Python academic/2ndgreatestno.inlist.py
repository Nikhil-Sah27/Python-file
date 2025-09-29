a = []
s = 0
while True:    
    n =(input('Enter a no.'))
    if n=="":
        break
    else:
        a.append(int(n))
b = 0
for i in range(len(a)):
    if a[i]>s:
        s = a[i]
for i in range(len(a)):
    if a[i]<s and a[i]>b:
        b = a[i]
print(b)        


        