# Number Guessing Game:
# Develop a game where the computer randomly selects a number, and the user has to guess it within a certain number of attempts.

import numpy as np
import numpy.random as r


def Guess():
    guess_number = r.randint(10)
    count = 0
    while True:
        try:
            user_number = int(input("Enter your guessing number b/w (0-9):"))
            count += 1
            if user_number == guess_number:
                print("Congratulations your guessing is Correct")
                break
            else:
                if user_number > guess_number:
                    print("Your Number is greater than Random Number")
                else:
                    print("Your Number is lower than Random Number")
                print(f"{count} Wrong guess, try again!")

        except ValueError:
            print("Enter Numerical Value Only")

    print(f"The correct number was: {guess_number}")
    print(f"You guessed {user_number} in {count} attempts.")


print("Welcome to play Number Guessing Game")
while True:
    user = input("Are you ready to play (Yes/No)? ").strip()
    if user.upper() == "YES":
        Guess()
    elif user.lower() == "no":
        print("Thank you for playing!")
        break  # Exit the loop if the user does not want to play
    else:
        print("Please enter a valid input (Yes or No).")
