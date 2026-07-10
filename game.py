import random

def play_game():
    secret_number = random.randint(1, 100)
    guess = None

    print("Welcome to Number Ninja!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != secret_number:
        guess = int(input("Your guess: "))

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print("You got it!")

if __name__ == "__main__":
    play_game()