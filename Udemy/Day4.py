# search random - generate pseudo-random numbers in python to learn random module


import random            # random module

random_integer = random.randint(1,20)
print(random_integer)


                # first create a file like my_module then call it in other file with the same name as my_module
import my_4module
print(my_4module.my_favourite_number)


print("\n")


random_number_0_to_1= random.random()   # gives float values from 0 to 1
print(random_number_0_to_1)


random_number_0_to_1= random.random()*10   # gives float values from 0 to 10
print(random_number_0_to_1)


print("\n")

random_float = random.uniform(1,10) # gives float with some integer like 9.888
print(random_float)

print("\n\n")


# Heads or tails


import random
integer=random.randint(0,1)
if integer==0:
    print("Heads")
else:
    print("Tails")
