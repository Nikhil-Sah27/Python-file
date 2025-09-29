# try:
#     list=[1,2,5,7,8,9]
#     b=int(input("Enter the index of list"))
#     print(list[b])
# except:
#     print("some error occured")
# finally:
#     print("I am always executed")



# def fun1():
#     try:
#         list=[1,2,5,7,8,9]
#         b=int(input("Enter the index of list"))
#         print(list[b])
#     except:
#         print("some error occured")
#     # finally:
#     print("I am always executed")
# fun1()


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
print(x)