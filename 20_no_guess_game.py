# 🔥 Q20 – Guess the Number Game
# Generate a random number between 1–100.
# User keeps guessing until correct.
# Tell them:
# Too high    Too low    Correct
# 💡 Use random module

import random

comp_choice = random.randint(1, 100)
no_of_guess = 0

while True:
    try:
        user_guess = int(input("Enter your guess :"))
    except (ValueError, TypeError) as e:
        # print("Error :",e)
        print("Please enter a valid number :")
        continue

    no_of_guess += 1

    if user_guess > comp_choice:
        print("Too high !!")

    elif user_guess < comp_choice:
        print("Too low !!")
    else:
        print("Correct !!")
        break


print(f"You guessed the right answer in {no_of_guess} no. of guesses .")
