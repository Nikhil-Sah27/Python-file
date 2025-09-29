         #Break
#Break is use to skip the further loops

for i in range(1,13):
    print("5 X",i,"=",5*i)
    if(i>10):  #will print up to i =11 because before reaching to condition(i>10), it has already printing command
         break
    

print("\n\n")

for i in range(1,13):
    if(i>10):  
         break
    print("5 X",i,"=",5*i)
  
print("\n\n")

for i in range(1,13):
    if(i>10):  
         break
    else:
         print("table of 5")
    print("5 X",i,"=",5*i)


print("\n\n")


#continue
#Continue is used to skip that particular loop


for i in range(1,14):
    if(i==11):
     print("example of continue")
     continue
    print("9 X",i,"=",i*9)



for i in range(1,14):
  if(i==11):
     print("example of continue")
     continue
  else:
    print("9 X",i,"=",i*9)
   


# i=0
# while True:   #False will not execute the code in place of True
#     print(i)   #the code is for infinite numbers
#     i=i+1

#in this program we will add some conditions and the code will turn similar to Do while loop


#similar to Do while loop

print("\n")

i=0
while True:   
     print(i)   
     i=i+1
     if(i%100==0):
         break
     
     
     


     


