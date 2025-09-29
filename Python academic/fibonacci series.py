a = 0
b = 1
n = int(input("Enter the nth value"))
if (n>0):
    print(a)
    print(b)  
    while(n>=3):
        c=a+b
        print(c)
        a=b
        b=c 
        n=n-1
else:
    print("The given no. is not valid")