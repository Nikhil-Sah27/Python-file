
f = open("Nikhil.txt","r")
text=f.read()
print(text)
f.close()

# Writting A File

f = open("Nikhil.txt",'w')
f.write("Hello,world! Its me Nikhil Sah. I am an CSE student")
f.close()

with open('Nikhil.txt','a') as f:
    f.write("Hey, I am Nikhil Sah.")