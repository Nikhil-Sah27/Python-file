# import time
 
# def count(end,start=0):
#     for x in range(start,end+1):
#         print(x)
#         time.sleep(1)  #It pauses the program for 1 second
#     print("Done!")

# count(10)

while True: 
 try:
    number = int(input("Enter the number"))
    print(1/number)
 except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")
 except ValueError:
    print("Enter only numbers please!")
 except Exception:
    print("Something went wrong!")
 finally:
    print("Do some cleanup here")