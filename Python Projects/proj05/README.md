# Number Guessing Game (Python Mini Project)

## Project Overview
This is a simple **Python Number Guessing Game** where the computer randomly selects a number between 1 and 100, and the user has to guess it.  
After each guess, the program gives hints — whether the guess is too high or too low — until the correct number is guessed.

---

## Features
- Generates a **random number** between 1 and 100 using `random.randint()`.
- Provides **real-time hints** ("Too high" / "Too low").
- Counts and displays the **total number of attempts**.
- Handles invalid (non-numeric) inputs gracefully.

---

## How It Works
1. The computer secretly picks a random number between 1 and 100.
2. You enter guesses until you find the correct number.
3. After each guess:
   - You get feedback whether your guess is **too high** or **too low**.
4. Once you guess correctly, the game displays how many attempts it took.

---

## Example Run
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100...
Enter your guess: 45
Too low! Try a higher number.

Enter your guess: 78
Too high! Try a lower number.

Enter your guess: 67
Congratulations! You guessed the number 67 in 3 attempts.

---

## How to Run
1. Save the code in a file named `number_guessing_game.py`.
2. Open your terminal or command prompt.
3. Run:
   ```bash
   python number_guessing_game.py

---