# Assignment 1: Guessing Game
# Murun T.
import random
from os import system, name 

# the playbool flag keeps track if the user wants to end the game
playbool = True

# fancy function to clear the terminal for new game
def clear(): 
  
    # clear terminal for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # clear terminal for mac and linux
    else: 
        _ = system('clear') 

while(playbool):
    # At the start of a game, reset stats
    count = 0

    # Choose a random number from 1 to 100, inclusive
    randomNumber = random.randint(1, 101)
    print("I will guess a number between 1 and 100.\nYou will have to guess my number.")
    guess = int(input("Enter your guess: "))
    count = count + 1

    # loop to keep getting new guesses and provided feedback each time until the guess is right
    while(randomNumber != guess):
        if(guess > randomNumber):
            print("Too high")
        else:
            print("Too low")
        # Ask for a new guess
        guess = int(input("Enter your guess: "))
        count = count + 1
    
    # When the guess is right, ask the user if they want play again. If the user wants to play again, the outer loop restarts.
    # If not, the program reaches the end.
    print("You guessed my number! It was: " + str(randomNumber))
    print("You guessed " + str(count) + " times!")
    again = input("Do you want to play again? Y/N")
    if(again == "Y"):
        playbool = True
        print("\n\n")
        clear() 
    else:
        playbool = False
        print("Thanks for playing!")

