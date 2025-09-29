#strings are immutable
a = "Nikhil"
print(a.upper())
print(a.lower())

b = "!!Nikhil!!!!!"
print(b.rstrip("!"))
print(b.replace("Nikhil","Harry")) #replaces Nikhil with Harry

c = "Nikhil Sah CSE7 807T"
print(c.split())


c = ["!","@","#","$","%","^","&","*"]
join_fun = "".join(c)
print(join_fun)
c = ["!","@","#","$","%","^","&","*"]
join_fun = "-".join(c)
print(join_fun)


a = "Nikhil"
s=list(a)
print(" ".join(s))


d = "nikhil SAh Is in CSE7"
print(d.capitalize()) # first letter of sentence will be capital and other will be small

e = "BMSIT"
print(e.center(50)) # moves toward center
print(len(e.center(50))) #gives the length of spaces

f = "I live in Bengaluru. Bengaluru is an It hub."
print(f.count("Bengaluru")) #counts repetation of letter

g = "I live in Bengaluru. Bengaluru is in India"
print(g.endswith("."))
h = "I live in Bengaluru , Bengaluru is in India."
print(h.endswith("."))
print(h.endswith("in",6,8))
print(h.endswith("in",3,9))

h = "I live in Bengaluru. Bengaluru is in India,"
print(h.find("Bengaluru"))
print(h.find("home")) # output -1 means doesn't find

print(h.index("is"))# if stirng not found then shows valueError: substring not found 
#ex: 
# print(h.index("home")) 


i = "nikhilSAhIsinCSE7"
print(i.isalnum()) # returns true if entire string consists of a-z, A-z and 0-9
 #if there is space in letters it will print false

j= "nikhilSAhIsinCSE" 
print(j.isalpha()) # returns true if entire string consists of a-z and A-z 
#if there is space in letters it will print false

print(j.islower()) #checks every letter is lower case or not

k = "nikhilSAhIsinCSE\n" 
print(k.isprintable()) #returns true if every character is printable
#Here, \n is not printable as it is inbuilt function

l = "       "
print(l.isspace())
l= " a   "
print(l.isspace())

m = "World Health Organization"
print(m.istitle()) #returns true only if the first letter of each word is capitalized.
m = "To kill a Mocking bird"
print(m.istitle())

e = "BMSIT"
print(e.isupper()) # returns true only if all the character in string is upper case

n = "strings are immutable"
print(n.startswith("strings")) #returns true if string starts with the given character

o = "World Health Organization"
print(o.swapcase()) #turns upper case into lower case

p= "To kill a Mocking bird"
print(p.title())  #converts sting into title

q = "Nikhil"
if "Nik" in q:
    print("\n yes")
else:
    print("\n\n no")


a = "Nikhil"*2  #the operator is used as string repetator string
print(a)


str = "Hello"
print(str[1])
print(str[-1])
print(str[1:3])

def right(s):
    print(s.rjust(70)) # last letter of string will be at 70th position(column) in a single row
string=input('enter a string')
right(string)

