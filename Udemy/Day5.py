for i in range(1,101):
 if i%3==0 and i%5==0:
    print("FizzBuzz")
 elif i%5==0:
    print("Buzz")
 elif i%3==0:
    print("Fizz")
 else:
    print(i)


# Password generator

print("Welcome to the PyPassword Generator!")


import random

password_list = []
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
symbols = ["!","@","#","$","%","^","&","*"]
numbers = ["1","2","3","4","5","6","7","8","9","0"]

letter=int(input("How many letters you want in your password"))
symbol=int(input("How many symbol you want in your password"))
number=int(input("How many number you want in your password"))

for i in range(0,letter): 
    password_list.append(random.choice(letters))   


for i in range(0,symbol): 
    password_list.append(random.choice(symbols)) 

for i in range(0,number): 
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password ="".join(map(str,password_list)) #if no. are there in list then join fun. is used as given else: "".join(password_list)
print(password)

# or 

password = ""
for char in password_list:
    password += char
print(f"Your password is {password}")