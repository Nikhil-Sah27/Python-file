fp = open("Nikhil.txt","r")
text=fp.readlines()
list=[]
for line in text:
    for word in line.split():
        list.append(word)
list.sort()
print(list)
fo=open("sah.txt","w")
for word in list:
    fo.write(word+"\n")
fo.close()