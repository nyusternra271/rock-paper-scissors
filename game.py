import random

# Print the welcome screen
print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print('-------------------')

# Set up the valid options list for validation and random selection later
valid_options=["rock", "paper", "scissors"]

# get the user's preference

user_input=input("Please choose either 'rock', 'paper', or 'scissors':")
computer_selection=random.choice(valid_options)
if not user_input.lower() in valid_options:
   print("You entered an invalid choice. Please rerun the program and select 'rock', 'paper', or 'scissors'")
   exit()
else:
    print('You chose: '+user_input)
    print('The computer chose: ' + computer_selection)
    print('-------------------')

    if user_input.lower() == computer_selection:
        print("The game ended in a draw")
        print('-------------------')
        print('Thanks for playing. Please play again')
        exit()
    elif (user_input.lower() == "rock" and computer_selection == "scissors") or (user_input.lower() == "paper" and computer_selection == "rock"):
        print("Congrats! You won!")
        print('-------------------')
        print('Thanks for playing. Please play again')
        exit()
    else:
        print("Sorry, the computer won this time")
        print('-------------------')
        print('Thanks for playing. Please play again')