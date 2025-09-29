a = int(input("Enter your age:"))
if(a>=18):
    print("you can drive")
else:
    print("you can't drive") #space before print is called indentation


appleprice= 210
budget=int(input("enter your budget"))
if(budget>=appleprice):
    print("Alexa add 1 kg apples to the cart")
else:
        print("Alexa don't add apple to the cart")


appleprice= 210
budget=int(input("enter your budget"))
c = budget//appleprice
if(budget>=appleprice):
    print("Alexa add" , c ,"kg apples to the cart")
else:
        print("Alexa don't add apple to the cart")



a=int(input("enter the value of a:"))
if(a<0):
    print("entered no. is negative.")
elif(a==0):
        print("Number is 0.")
else:
        print("the no. is positive.")

        
# Nested if statements

b=int(input("Enter value"))
if(b<0):
      print("entered no. is negative")
elif(b>0):
      if(b<=10):
            print("the no. is between 1 and 10")
      elif(b>10 and b<=20):
            print("the no. is between 10 and0 20")
      else:
            print("the no. is greater than 20")
else:
      print("the no. is zero")

        
 
       