marks  = [1,14,59,11,45]
marks.append(9)
print(marks)


marks.sort()#arrange in ascending order 
print(marks) 

marks.sort(reverse=True) #arrange in descending order
print(marks)

marks = [1,14,59,11,45]
marks.reverse()
print(marks)


marks = [1,14,59,11,45,11]
print(marks.index(11)) #returns the index of the first occurance.


marks = [1,14,59,11,45,11]
print(marks.count(11))

print("\n\n")

l = marks 
l[0]= 0 
print(marks)


print("\n")

marks = [1,14,59,11,45]
l = marks.copy()
l[0] = 0
print(marks)
print(l)

print("\n")
marks.insert(2,100)
print(marks)

print("\n")
l = [33, 44 , 75, 92]
marks.extend(l)
print(marks)
# or
marks = [1,14,59,11,45]
k = marks + l
print(k)

print("\n")

marks = [1,14,59,11,45]
marks.pop(1)
print(marks)

print("\n")

spam = ["cat",'bat','rat','elephant','dog']
spam[4] = 'hello'
print(spam)

spam[1]=spam[3]
print(spam)

del spam[4]
print(spam)


print('cat'  in ["cat",'bat','rat','elephant','dog'])
print('bat' not in ["cat",'bat','rat','elephant','dog'])


spam = ["cat",'bat','rat','elephant','dog']
print(spam.index("rat"))


spam.append("Moose")
print(spam)

spam.insert(2,"chicken")
print(spam)

spam.remove("dog")
print(spam)

del spam[2]
print(spam)