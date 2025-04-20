#Rock-paper-scissors game
# This is a simple rock-paper-scissors game where the user inputs their choice and the computer randomly selects one.
# The program then compares the two choices and determines the winner.
import random 
print(" ")
userInput = input("Enter rock, paper, or scissors: \n")
choices = ["rock", "paper", "scissors"]
computerInput = random.choice(choices)
print(f"Computer chose: {computerInput}")
if userInput == computerInput:
    print("It's a tie!")
elif userInput == "rock":
    if computerInput == "paper":
        print("You lose!")
    else:
        print("You win!")
elif userInput == "paper":
    if computerInput == "scissors":
        print("You lose!")
    else:
        print("You win!")
elif userInput == "scissors":
    if computerInput == "rock":
        print("You lose!")
    else:
        print("You win!")