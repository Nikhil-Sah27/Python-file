 # lists are ordered collection of data items.
 #They store multiple items in a single variable.
 #List items are seperated  by commas and enclosed within square brackets.
 #Lists are changeable meaning we can alter them after creation.



marks = [3,5,6,True,"Nikhil"]  #lenth of mark is 5 but index is 4
print(marks)
print(type(marks))
print(marks[0])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[-4]) #or print(marks[len(marks)-4])

if "Nikhil" in marks:
     print("\n\nyes")
else:
     print("\n\nNO")

print(marks[:]) # or print(marks[0:len(marks)])
print(marks[1:])
print(marks[:3])
print(marks[1:-2])
print(marks[0:5:2])


lst= [i for i in range(4)]
print(lst)   

lst= [i*i for i in range(4)]
print(lst)   


lst= [i for i in range(10) if i%2==0]
print(lst)   