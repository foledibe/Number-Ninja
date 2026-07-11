import random

DIFFICULTIES = {
    "1": {"name": "Easy", "range": 50, "attempts": 10},
    "2": {"name": "Medium", "range": 100, "attempts": 7},
    "3": {"name": "Hard", "range": 200, "attempts": 5},
}

def choose_difficulty():
    print("\nChoose a difficulty:")
    print("1) Easy   (1-50, 10 guesses)")
    print("2) Medium (1-100, 7 guesses)")
    print("3) Hard   (1-200, 5 guesses)")

    choice = input("Enter 1, 2, or 3: ")
    return DIFFICULTIES.get(choice, DIFFICULTIES["2"])

def get_valid_guess(low, high):
    """Keep asking until the player types a real number in range."""
    while True:
        raw_input_value = input(f"Your guess ({low}-{high}): ")
        try:
            guess = int(raw_input_value)
        except ValueError:
            print("That's not a number — try again.")
            continue

        if guess < low or guess > high:
            print(f"Pick a number between {low} and {high}.")
            continue

        return guess

def play_game():
    print("Welcome to Number Ninja!")
    difficulty = choose_difficulty()

    secret_number = random.randint(1, difficulty["range"])
    attempts_left = difficulty["attempts"]

    print(f"\nI'm thinking of a number between 1 and {difficulty['range']}.")
    print(f"You have {attempts_left} guesses. Good luck!\n")

    while attempts_left > 0:
        guess = get_valid_guess(1, difficulty["range"])
        attempts_left -= 1

        if guess < secret_number:
            print(f"Too low! ({attempts_left} guesses left)")
        elif guess > secret_number:
            print(f"Too high! ({attempts_left} guesses left)")
        else:
            print("🎉 You got it!")
            return

    print(f"\nOut of guesses! The number was {secret_number}.")

if __name__ == "__main__":
    play_game()