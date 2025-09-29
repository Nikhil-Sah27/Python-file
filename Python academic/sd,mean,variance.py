from math import sqrt
list=[]
n=int((input("Enter the no. of terms")))
for i in range(n):
    num=input("Enter a number")
    list.append(int(num))
total=0
for elem in list:
    
    total=total+elem
mean=total/int(n)

total=0
for elem in list:
    total=(total-elem)*(total-elem)
variance=total/int(n)
sd=sqrt(variance)
print(mean)
print(variance)
print(sd)
