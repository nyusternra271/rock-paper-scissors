
# Rock Paper Scissors Game
## Description
This is a simple game of rock-paper-scissors in which you compete against the computer to see who wins according to the following rules:
1. Rock beats Scissors
2. Paper beats Rock
3. Scissors beats Paper

The game ends in a draw if you and the computer both pick the same selection (i.e., Rock-vs-Rock, Paper-vs-Paper, Scissors-vs-Scissors)

## Environment Setup
In order to run this game, you'll need to set up your environment appropriately. These instructions assume that you have already installed anaconda on your device of choice. To set up your environment, run the following command:

    conda create -n rock-paper-scissors python=3.8

Python versions 3.9 and 3.10 will also work.

## Running the Game
After setting up your environment, activate it by running the following command:

    conda activate rock-paper-scissors

Once the environment has been activated, you can run the game as follows:

```sh
python game.py
```
You will be prompted to enter a selection (case does not matter). You should see the following:
```
-------------------
Welcome 'Player One' to my Rock-Paper-Scissors game...
-------------------
Please choose either 'rock', 'paper', or 'scissors':rock
You chose: rock
The computer chose: rock
-------------------
The game ended in a draw
-------------------
Thanks for playing. Please play again
```


The game will end abruptly with an error if you don't make a valid selection:
```
-------------------
Welcome 'Player One' to my Rock-Paper-Scissors game...
-------------------
Please choose either 'rock', 'paper', or 'scissors':water
You entered an invalid choice. Please rerun the program and select 'rock', 'paper', or 'scissors'
```

