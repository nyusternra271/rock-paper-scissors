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
else:
    print(f"You chose: {user_selection}")
    print(f"The computer chose: {computer_selection}")
    print('-------------------')

# compare the user's choice to the computer's choice and determine the winner according to the rules of the game:
#
if user_selection.lower() == computer_selection:
    print("The game ended in a draw")
    print('-------------------')
    print('Thanks for playing. Please play again')
    exit()
elif (user_selection.lower() == "rock" and computer_selection == "scissors") or (user_selection.lower() == "paper" and computer_selection == "rock"):
    print("Congrats! You won!")
    print('-------------------')
    print('Thanks for playing. Please play again')
    exit()
else:
    print("Sorry, the computer won this time")
    print('-------------------')
    print('Thanks for playing. Please play again')