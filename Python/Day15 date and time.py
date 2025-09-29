import time
a = time.strftime('%H:%M:%S')
print(a)
b=int(time.strftime('%H'))
if(b<12):
    print("Good Morning, Sir")
elif(b>=12 and b<17):
    print("Good Afternoon, Sir")
elif(b>=17 and b<20):
    print("Good Evening, Sir")
else:
    print("Good Night, Sir")


print("\n\n")

# For 12 Hour clock

import time
a = time.strftime('%I:%M:%S')
b = time.strftime('%p')
print(a,b,sep=" ") #space is used here to space between time and am or pm
c = int(time.strftime('%I'))
if(b.endswith("PM")):
   if(c==12):
     print("Good Afternoon, Sir")
   elif(c<5):
     print("Good Afternoon, Sir")
   elif(c>=5 and c<8):
     print("Good Evening, Sir")
   else:
     print("Good Night, Sir")
else:
 print("Good Morning")

 
    