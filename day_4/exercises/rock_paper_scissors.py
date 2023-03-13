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

#Write your code below this line 👇

import random

# store possible options in a corresponding variable
possible_option = [rock, paper, scissors]

# prompt user for choice of object
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: "))
print(player_choice)
print(possible_option[player_choice])

# store computer's choice according
computer_choice = random.randint(0, 2)

print("Computer chose:\n")
print(possible_option[computer_choice])

if player_choice == 0 and computer_choice == 1:
    print('You lose.')
elif player_choice == 1 and computer_choice == 2:
    print('You lose.')
elif player_choice == 2 and computer_choice == 0:
    print('You lose')
elif player_choice == 1 and computer_choice == 0:
    print('You win')
elif player_choice == 2 and computer_choice == 1:
    print('You win')
elif player_choice == 0 and computer_choice == 2:
    print('You win')
else:
    print('It is a draw')
    
    