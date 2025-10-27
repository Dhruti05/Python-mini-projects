# Project 5: Number Guessing game
# A fun python program where the user tries to gess a randomly generated number.
# The program provides hints ("to high or to low") until the correct guess is made.

import random

def number_guessing_game():
    print("Welcome to number guessing game")
    print("I'm thinking of a number between 1 to 100...")

    #Generate a random target number
    target_number = random.randint(1,100)
    attempts = 0 #counter for attempts

    while True:
        try:
            #Ask user to guess the number
            guess = int(input("Enter your guess:"))
            attempts += 1

            #compare guess with the target number
            if guess < target_number:
                print("Too low! Try a higher number.")
            elif guess > target_number:
                print("Too high! Try a lower number.")
            else: 
                print(f"Congratulations!! You have guess it right in {attempts} attempts!!")
                break
        except ValueError:
            print("Invalid input! Please enter the number between 1 to 100")

if __name__ == "__main__":
    number_guessing_game()