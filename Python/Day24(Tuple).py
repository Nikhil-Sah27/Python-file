#Tuples are ordered collection of same type data items.
#Tuples are unchangeable

tup=(1,)
print(type(tup))

tup = (1,2,4,5, "Tree",True)
print(type(tup),tup)
print(tup[2])
print(tup[4])
print(tup[5])
print(tup[-2])

if 2 in tup:
    print("yes")
else:
    print("NO")

#same properties as list

print(2 in tup)