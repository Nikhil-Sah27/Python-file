a = 9
b = 8
gmean1 = (a*b)/(a+b)
print(gmean1)

c = 8
d = 7
gmean2 = (c*d)/(c+d)
print(gmean2)



# Using Function

def calculategmean(a,b):
    gmean=(a*b)/(a+b)
    print(gmean)

a = 9
b = 8
calculategmean(a,b)

c = 8
d = 7
calculategmean(c,d)

print("\n\n")


def greaterfun(a,b,c):
    if(a>b and a>c):
        print("a is greater")
    elif(b>c and b>a):
        print("b is greater")
    elif(c>a and c>b):
        print("c is greater")
    else:
        print("any number is equal")
    #upper part is called function definition



a = 9
b = 6
c= 19
greaterfun(a,b,c)

a = 7          #its called over writting of variable
d = 24
e =15
greaterfun(a,d,e)



print("\n\n")


def islesser(a,b):
    pass



print("pass means this fun. will be written later, u should continue executing next prgm.")



