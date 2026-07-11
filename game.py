import random
import json
import os

DIFFICULTIES = {
    "1": {"name": "Easy", "range": 50, "attempts": 10},
    "2": {"name": "Medium", "range": 100, "attempts": 7},
    "3": {"name": "Hard", "range": 200, "attempts": 5},
}

SCORES_FILE = "high_scores.json"

def load_high_scores():
    if not os.path.exists(SCORES_FILE):
        return {}
    with open(SCORES_FILE, "r") as f:
        return json.load(f)

def save_high_scores(scores):
    with open(SCORES_FILE, "w") as f:
        json.dump(scores, f, indent=2)

def update_high_score(difficulty_name, attempts_used):
    scores = load_high_scores()
    current_best = scores.get(difficulty_name)

    if current_best is None or attempts_used < current_best:
        scores[difficulty_name] = attempts_used
        save_high_scores(scores)
        return True  # new record!
    return False

def choose_difficulty():
    print("\nChoose a difficulty:")
    print("1) Easy   (1-50, 10 guesses)")
    print("2) Medium (1-100, 7 guesses)")
    print("3) Hard   (1-200, 5 guesses)")

    choice = input("Enter 1, 2, or 3: ")
    return DIFFICULTIES.get(choice, DIFFICULTIES["2"])

def get_valid_guess(low, high):
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
    total_attempts = difficulty["attempts"]
    attempts_left = total_attempts

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
            attempts_used = total_attempts - attempts_left
            print(f"🎉 You got it in {attempts_used} guesses!")

            is_record = update_high_score(difficulty["name"], attempts_used)
            if is_record:
                print("🏆 New high score for this difficulty!")
            return

    print(f"\nOut of guesses! The number was {secret_number}.")

def main():
    print("=" * 40)
    print("           NUMBER NINJA 🥷")
    print("=" * 40)

    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing! 👋")
            break

if __name__ == "__main__":
    main()