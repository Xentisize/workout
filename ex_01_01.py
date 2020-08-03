# Number guessing game

import random

computer_choice = random.randint(0, 100)


def guess_game() -> str:
    # Guessing game for user to guess the amount of a random number
    while user_guess := input("What is your guess: "):
        user_guess = int(user_guess)
        if user_guess == computer_choice:
            print("You are correct.")
            print(f"The number is {computer_choice}.")
            break
        if user_guess < computer_choice:
            print("Your guess is too small.")
            continue
        if user_guess > computer_choice:
            print("Your guess is too large.")
            continue


if __name__ == "__main__":
    guess_game()
