import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("\nI'm thinking of a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
            elif guess < number_to_guess:
                print("Too low! Try again.")
            elif guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter an integer.")

def number_guessing_game():
    print("🎮 Welcome to the Number Guessing Game!")

    while True:
        play_game()
        choice = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Thanks for playing! Goodbye!")
            break

# Run the game
number_guessing_game()
