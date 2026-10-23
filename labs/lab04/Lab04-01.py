# Starting file for LAB 4-1
# CS31 Course
# Carlos Farias
# Date 10/22/2026

#============================================
#        Guess the Number
#============================================
# Practice program: use functions.

import random

## 1. Displays the game title 
def display_title():
    print("Guess the number!")
    print()

## 2. Asks for the player's name, greets them, and RETURNS it
def get_name():
    player_name = input("What is your name?  ")    
    print("Hello", player_name)
    print()

## 3. Asks for a difficulty level until the input is valid
def get_level():
    while True:
        level = input("What game level would you like to play? E for Easy, M for Moderate, or H for Hard: ")
        if level.lower() in ["e", "m", "h"]:
            return level
        else:
            print("Sorry. Invalid input. Please try again.\n")

## 4. Plays one round of the game and updates the score
def play_game(wins, losses):
    level = get_level()

    if level.lower() == "e":
        max_number = 10
        tries = 5
    elif level.lower() == "m":
        max_number = 100
        tries = 8
    elif level.lower() == "h":
        max_number = 1000
        tries = 10
    else:
        print("Sorry. Invalid input. Please try again.\n")
        return wins, losses  # Return current scores unchanged if input is invalid

    number = random.randint(1, max_number)
    print(f"I'm thinking of a number from 1 to {max_number}\n")
    
    count = 1
    while count <= tries:
        guess = int(input("Your guess: "))
        if guess < number:
            print("Too low.")
            count += 1
        elif guess > number:    
            print("Too high.")
            count += 1
        else:
            print(f"You guessed it in {count} tries!\n")    
            wins += 1
            print(f"Score - Wins: {wins}, Losses: {losses}")
            return wins, losses
    
    # If the loop finishes without returning, the player ran out of tries (Loss)
    print(f"Sorry. You ran out of guesses. The number was {number}.")
    losses += 1
    print(f"Score - Wins: {wins}, Losses: {losses}\n")
    return wins, losses

## 5. Runs the whole program and keeps the score
def main():
    display_title()
    get_name()
    
    # Initialize variables for requirement (4)
    wins = 0
    losses = 0
    again = "y"
    
    while again.lower() == "y":
        wins, losses = play_game(wins, losses)
        again = input("Would you like to play again? (y/n): ")
        print()
        
    print(f"Final Score -> Wins: {wins}, Losses: {losses}")
    print("Thank you!!")    

# If started as the main module, call the main function
if __name__ == "__main__":
    main()