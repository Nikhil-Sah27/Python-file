#Who will pay the bill



friends=["Nikhil","Suyash","Aayush","Kaushal","Manish","Aryan","Manik"]
import random 
random_no = random.randint(0,len(friends))
print(f'{friends[random_no]} will pay the bill')


print("\n")


# OR



import random
friends =["Nikhil","Suyash","Aayush","Kaushal","Manish","Aryan","Manik"]
print(f'{random.choice(friends)} will pay the bill')


