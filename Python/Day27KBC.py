# Create a program capable of displaying questions to the user like KBC.
# Use list data type to store the questions and their correct answers.
# Display the final amount the person is taking home after playing the game.



s=0
q = ["highest peak of earth","Nepal's capital city","National animal of nepal","Nepalese food","Nepal,s GDP"]
qa = ["Mt. Everest","Kathmandu",'Cow',"Ghundruk","46 billion$"]
p = [1000,10000,30000,100000,1000000]
ops= [['a.Mt. Everest','b.Mt.Machapuchre','c.Mt.Annapurna',"d.Mt. Fuji"],['a.Pokhara',"b.Kathmandu",'c.Birgunj','d.Lalitpur'],['a.Cow',"b.Lion",'c.Panda','d.Peacock'],['a.Dhido','b.Ghundruk','c.selroti','d.Dalbhat'],['a.10 billion$','b.90 billion$',"c.46 billion$",'d.49 billion$']]
for i in range(len(q)):
    print(q[i]) 
    print(ops[i])
    ans =input("Enter your answer")
    if ans=='a':
       if ops[i][0].endswith(qa[i]):
        print("Bilkul Sahi Jawab")
        s = s+p[i]
        print("You won",s)
        print("You wanna play more")
        choose = input("yes or no")
        if choose=="yes":
          continue
        else:
          break
       else:
        print("galat jawab")
        print("You won total",s)
        break
    elif ans=='b': 
       if ops[i][1].endswith(qa[i]):
        print("Bilkul Sahi Jawab")
        s = s+p[i]
        print("You won",s)
        print("You wanna play more")
        choose = input("Yes or No")
        if choose=="yes":
          continue
        else:
          break
       else:
        print("galat jawab")
        print("You won total",s)
        break        
    elif ans=='c':
       if ops[i][2].endswith(qa[i]):
        print("Bilkul Sahi Jawab")
        s = s+p[i]
        print("You won",s)
        print("You wanna play more")
        choose = input("Yes or No")
        if choose=="yes":
          continue
        else:
          break
       else:
        print("galat jawab")
        print("You won total",s)
        break
    elif ans=='d':
       if ops[i][3].endswith(qa[i]):
        print("Bilkul Sahi Jawab")
        s = s+p[i]
        print("You won",s)
        print("You wanna play more")
        choose = input("Yes or No")
        if choose=="yes":
          continue
        else:
          break
       else:
        print("galat jawab")
        print("You won total",s)
        break
    else:
        print("galat jawab")
        print("You won total",s)
        break
    
   

    