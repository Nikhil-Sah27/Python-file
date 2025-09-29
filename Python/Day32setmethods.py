s1= {1,2,4,6,8,7}
s2={1,2,3,4,5,6,7}
print(s1.union(s2))


print(s1,s2)


s3= {1,4,6,8,7}
s4={1,2,3,4,5}
s3.update(s4)
print(s3)
print(s4)


s3= {1,4,6,8,7}
s4={1,2,3,4,5}
print(s3.intersection(s4))

print('\n')

s3= {1,4,6,8,7}
s4={1,2,3,4,5}
s3.intersection_update(s4)
print(s3)

print('\n')

# Symmetric Difference [(A union B)-(A itersection B)]
# not common in both sets

s3= {1,4,6,8,7}
s4={1,2,3,4,5}
print(s3.symmetric_difference(s4))


s3= {1,4,6,8,7}
s4={1,2,3,4,5}
s3.symmetric_difference_update(s4)
print(s3)

print('\n')

s3= {1,4,6,8,7}
s4={1,2,3,4,5}
print(s3.difference(s4))
s3.difference_update(s4)
print(s3)

print("\n")


s3= {1,4,6,8,7}
s4={1,2,3,4,5}
print(s3.isdisjoint(s4))


s3= {1,4,6,8,7}
s4={0,2,3,5,9}
print(s3.isdisjoint(s4))

print("\n")
s3= {1,4,6,8,7,2,3,5,9,0}
s4={0,2,3,5,9}
print(s3.issuperset(s4))
print(s4.issubset(s3))


#add  

s3= {1,4,6,8,7}
s4={1,2,3,4,5}
s3.add(0)
print(s3)
  

  # Remove
s3= {1,4,6,8,7}
s4={1,2,3,4,5}
s3.remove(1)         # if there is no such value in s3 then remove function raises an eror
print(s3)

#Discard

s3= {1,4,6,8,7}
s4={1,2,3,4,5}
s3.discard(1)
s3.discard(0)
print(s3)              # discard doesn't raise any error


 # Pop
s3= {1,4,6,8,7}
s4={1,2,3,4,5}
a = s3.pop()  # any random value will be pop out
print(a)
 
#Del

s3= {1,4,6,8,7}
s4={1,2,3,4,5}
del s3              # Entire set will be deleted
#print(s3)

# clear

s3= {1,4,6,8,7}
s4={1,2,3,4,5}
s3.clear()            # clear just delete the entire elements inside the set
print(s3)

print("\n")

#Check if item exists

name = {"Nikhil","Suyash","Kaushal","Aayush"}
print("Nikhil" in name)