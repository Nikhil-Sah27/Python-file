def average(a,b):
    print("the average is:",(a+b)/2)

average(4,8)


def average(a=1,b=9):
    print("the average is:",(a+b)/2)

average()  #here a = 1 and b = 9 by default , called default argument


def average(a=1,b=9):
    print("the average is:",(a+b)/2)

average(9,7) #here it will accept a=9 and b=7


def average(a=1,b=9):
    print("the average is:",(a+b)/2)

average(5)       #here b value will be 9 by default


def average(a=1,b=9):
    print("the average is:",(a+b)/2)

average(b=5)


def average(a=1,b=9):
    print("the average is:",(a+b)/2)

average(b=5,a=13)



def average(*numbers):
    sum=0
    for i in numbers:
        sum = sum + i
    print("Average is:",sum/len(numbers))

average(5,6,7,3,10,8,2,1)


def average(*numbers):
    sum=0
    for i in numbers:
        sum = sum + i
    return sum/len(numbers)

c = average(5,6,7,3,10,8,2,1)
print(c)





def fun1():
    try:
        list=[1,2,5,7,8,9]
        b=int(input("Enter the index of list"))
        print(list[b])
    except:
        print("some error occured")
    finally:
        print("I am always executed")
x=fun1()
print(x)  # no return is in function. So "None" will be printed for print(x)


def fun1():
    try:
        list=[1,2,5,7,8,9]
        b=int(input("Enter the index of list"))
        print(list[b])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("I am always executed")
x=fun1()
print(x) # Here the returned values from definition part will be printed