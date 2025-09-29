#Pizza order Practice

print("Welcome to python pizza deliveries!")
size = input("What size pizza do you want? S,M or L:")
size=size.lower()
pepperoni= input("Do you want pepperonion your pizza? Y or N:")
pepperoni=pepperoni.lower()
extracheese=input("Do you want extra cheese on your pizza? Y or N:")
extracheese= extracheese.lower()
bill = 0
if size == "s":
    bill+=15
elif size=="m":
    bill+=20
elif size=="l":
    bill +=25
   
if pepperoni=="y":
    if size =="s":
        bill+=1
    elif size=="m":
        bill+=2
    elif size=="l":
        bill+=3
if extracheese=="y":
    bill+=2
print(f"Your total bill is: ${bill}.")



