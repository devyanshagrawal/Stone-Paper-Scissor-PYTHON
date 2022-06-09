import random


choice_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
list_choice = [i for i in range(3)]
randomChoice = random.choice(list_choice)

rock = '''
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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

if choice_user == 0:
    print("You choosed :\n",rock)

    if randomChoice == 0:
        print("Computer choosed :\n", rock)
        print("Draw!")
    elif randomChoice == 1:
        print("Computer choosed :\n", paper)
        print("You win!")   
    else:
        print("Computer choosed :\n", scissors)
        print("You lost!")
if choice_user == 1:
    print("You choosed :\n",paper)

    if randomChoice == 1:
        print("Computer choosed :\n", paper)
        print("Draw!")
    elif randomChoice == 0:
        print("Computer choosed :\n", rock)
        print("You win!")   
    else:
        print("Computer choosed :\n", scissors)
        print("You lost!")    
if choice_user == 2:
    print("You choosed :\n",scissors)

    if randomChoice == 2:
        print("Computer choosed :\n", scissors)
        print("Draw!")
    elif randomChoice == 1:
        print("Computer choosed :\n", paper)
        print("You win!")   
    else:
        print("Computer choosed :\n", rock)
        print("You lost!")               
