"""
How It Works:
    The program generates a random number between 1 and 100.
    The user keeps guessing until they get the right number.
    The program gives hints (Too Low / Too High).
    If the user enters anything other than a number, it catches the error and asks again.
    When the user guesses correctly, it displays the number of attempts taken.
"""
import random


def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Computer: I have selected a number between 1 and 100. Try to guess it!")

    secret_number = random.randint(1, 10)
    print("Secret number: ", )

    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess: ")) # Take user input
            # attempts = attempts + 1
            attempts += 1

            if guess < secret_number:
                print("Hint: Too low! Try agian.")
            elif guess > secret_number:
                print("Hint: Too high! Try agian.")
            else:
                print(f"Congratulations! You guessed the right number in {attempts} attempts")
                break # Exit the loop when the correct number is guessed
        except ValueError:
            print("Invalid input! Please enter a number")

# Run the game
number_guessing_game()