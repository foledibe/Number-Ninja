# 🎯 Number Ninja

A simple command-line number guessing game built with Python. The game lets players choose between different difficulty levels, gives hints after each guess, and saves the best scores so progress isn't lost after closing the program.

## Features

- 🎚️ Three difficulty levels (Easy, Medium, Hard)
- 💡 Higher/lower hints after every guess
- ✅ Input validation to prevent crashes from invalid input
- 🏆 High scores that are saved between game sessions
- 🔁 Option to play multiple rounds without restarting the program

## How to Play

```bash
python game.py
```

Choose a difficulty level, enter your guesses, and try to find the correct number in as few attempts as possible. After each guess, the game lets you know whether the number is higher or lower until you get it right.

## Tech Used

- Python 3
- JSON for data persistence

## What I Learned

Building this project made me rethink how I approach problems in code; instead of writing one long block that does everything, I broke it into smaller functions I could reuse and actually test individually. That shift alone made the whole thing easier to debug and reason about. Along the way I got a lot more comfortable using dictionaries to organize game data, and I started working with JSON files so the game could save progress and pick back up where it left off instead of resetting every time it ran.
The part that ended up mattering most was input validation. I hadn't realized how easily a program can break until I started testing it with weird, unexpected inputs: letters instead of numbers, blank entries, whatever a real user might actually type. Adding proper error handling fixed that, and it changed how I think about writing code in general: it's not just about getting the logic right, it's about accounting for what happens when someone doesn't use your program the way you expect. I also leaned on loops to keep gameplay going until the player either guessed correctly or chose to play again, which forced me to think more carefully about program flow and exit conditions.
By the end, I'd touched almost every core Python concept like functions, conditionals, loops, dictionaries, file handling, and exception handling, but the bigger takeaway was just having built something complete, start to finish, and having to make real decisions about structure and reliability along the way.
