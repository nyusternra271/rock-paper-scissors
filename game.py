# Import the random module which is needed for the computer choice
import random

# Print the welcome screen
print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print('-------------------')

# Set up the valid options list for validation and random selection later
valid_options=["rock", "paper", "scissors"]

# get the user's choice
user_selection=input("Please choose either 'rock', 'paper', or 'scissors':")

# get the computer's choice
computer_selection=random.choice(valid_options)

# validate the user's input
if not user_selection.lower() in valid_options:
   print("You entered an invalid choice. Please rerun the program and select 'rock', 'paper', or 'scissors'")
   exit()
# if a valid choice is made, print it out along with the computer's random selection
print(f"You chose: {user_selection}")
print(f"The computer chose: {computer_selection}")
print('-------------------')

# compare the user's choice to the computer's choice and determine the winner according to the rules of the game:
# 1. Rock beats Scissors
# 2. Scissors beats Paper
# 3. Paper beats Rock

if user_selection.lower() == computer_selection:
    print("The game ended in a draw")
    print('-------------------')
    print('Thanks for playing. Please play again')
elif (user_selection.lower() == "rock" and computer_selection == "scissors") or (user_selection.lower() == "paper" and computer_selection == "rock") or (user_selection.lower() == "scissors" and computer_selection=="paper"):
        print("Congrats! You won!")
        print('-------------------')
        print('Thanks for playing. Please play again')
else:
    print("Sorry, the computer won this time")
    print('-------------------')
    print('Thanks for playing. Please play again')