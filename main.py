# Assignment 1: Guessing Game
# Murun T.
import random
from os import system, name 

# the playbool flag keeps track if the user wants to end the game
playbool = True
count = 0

# fancy function to clear the terminal for a new game
def clear(): 
  
    # clear terminal for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # clear terminal for mac and linux
    else: 
        _ = system('clear') 

# Return a validated user input
def inputValidation():
    global count
    suspiciousInput = ""
    validInt = False
    inRange = False
    
    # Keep trying new input from user until it's a valid integer 1 - 100
    while(not validInt or not inRange):
        suspiciousInput = input("Give me a guess: ")
        count = count + 1
        validInt = suspiciousInput.isnumeric()
        if(not validInt):
            print("Integers 1 - 100 only!")
        else:
            suspiciousInput = int(suspiciousInput)
            if(isInRange(suspiciousInput)):
                inRange = True
            else:
                inRange = False
                print("Integers 1 - 100 only!")
        
    return suspiciousInput
    
# Helper function for inputValidation() to check is the integer is in range of 1 - 100. 
def isInRange(suspiciousInput):
    if((suspiciousInput > 0) and (suspiciousInput < 101)):
        return True
    else:
        return False

while(playbool):
    # At the start of a game, reset stats
    count = 0

    # Choose a random number from 1 to 100, inclusive
    randomNumber = random.randint(1, 101)
    print("I will guess a number between 1 and 100.\nYou will have to guess my number.")
    guess = inputValidation()

    # loop to keep getting new guesses and provided feedback each time until the guess is right
    while(randomNumber != guess):
        if(guess > randomNumber):
            print("Too high")
        else:
            print("Too low")
        # Ask for a new guess
        guess = inputValidation()
    
    # When the guess is right, ask the user if they want to play again. If the user wants to play again, the outer loop restarts.
    # If not, the program reaches the end.
    print("You guessed my number! It was: " + str(randomNumber))
    print("You tried " + str(count) + " times!")
    again = input("Do you want to play again? Y/N ")
    if(again == "Y"):
        playbool = True
        print("\n\n")
        clear() 
    else:
        playbool = False
        print("Thanks for playing!") 

