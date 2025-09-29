  # Match Case Statements

x = int(input("enter a no."))
#x is a variable to match
match x:
    case 0:
        print("x is zero")
    case 2: 
        print("case is 2")
    case 6 if x%2 == 0:
        print("X%2=0 and case is 6")
    case 5 if x>2:
        print("case is 5 and x > 2")
    case _ if x<10:
        print("x is smaller than 10")
    case _:
        print(x)