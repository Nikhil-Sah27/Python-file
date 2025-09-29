# subscripting
print("Hello"[0])


print(12_34565_9821)  # underscore is ignored and it is like commas used between no.  (9,123,456)


print('\n')

print(type(8/8))
print(type(8//4))

print(round(8/3))  #it round off the value
print(round(8/3,2))


#fstring
score = 0
height = 1.8
is_winning = True
print(f"Your score = {score},your height is {height},you gonna win is {is_winning}")

print('\n\n')


# Tip Calculator
print("Welcome to Tip Calculator")
Total_bill=float(input("Enter the bill\n"))
person_no = int(input("enter the no. of persons\n"))
tip_percent = float(input("Enter tip \n"))
each_bill = (Total_bill/person_no)*(1+tip_percent/100)
final_amount=round(each_bill,2)
print(f"Each person should pay: ${final_amount}")