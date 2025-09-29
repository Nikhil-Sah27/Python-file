import random


rock= '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''
paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''
scissor = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
''' 

list=["rock","paper","scissor"]
random_value = random.choice(list)

choice=input("Enter rock,paper or scissor\n")
print("\nComputer Choose")
print(random_value+"\n")

if choice == random_value:
    print("Draw")
elif choice == "rock" and random_value=="paper":
    print(paper)
    print('paper')
    print("You Loose")
elif choice == "rock" and random_value=="scissor":
    print(rock)
    print("rock")
    print("You win")
elif choice == "paper" and random_value=="rock":
    print(paper)
    print("paper")
    print("You win")
elif choice == "scissor" and random_value=="rock":
    print(rock)
    print("rock")
    print("You Loose")
elif choice == "scissor" and random_value=="paper":
    print(scissor)
    print("scissor")
    print("You win")
elif choice == "paper" and random_value=="scissor":
    print(scissor)
    print("scissor")
    print("You Loose")
else:
    print("Enter properly")
