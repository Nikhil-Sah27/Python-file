countries = ("Nepal","India","USA","Japan","Spain","Germany","Korea","Austrslia")
temp = list(countries)
temp.append("Russia")
temp.pop(5)  #pop is used to delete the element from string
temp[3]="UK"
countries = tuple(temp)
print(countries)

print("\n\n")

countries1= ("Nepal","India","Bangladesh","Pakistan")
countries2= ("China","srilanka","Russia")
asian= countries1 + countries2
print(asian)

print("\n\n")


tuple1 = (1,0,8,4,2,0,1,2,3,2,7,5,6,9)
print(tuple1.count(2))
print(tuple1.index(3))    #gives the position of the element
print(tuple1.index(2,5,10))   #gives the pos of elements from between index 5-10 
print(len(tuple1))
