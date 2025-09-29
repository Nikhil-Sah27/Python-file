def fact(n):
    if n == 0 or n==1:
        return 1
    else:
        return n*fact(n-1)

a =fact(5)                 # or print(fact(5))
print(a)


print("\n\n")


# find fibonacci series using recursion


a = 0
b = 1
c = 0
print(a)
print(b)
def fibb(n):
    global a,b,c
    if n<3:
        return 0
    else:
        c=a+b
        print(c) 
        a=b
        b=c        
        return fibb(n-1)


fibb(10)