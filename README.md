# python-todo-json
practice repository for python begginers

A smart number-guessing game built in Python, inspired by "Akinator". The computer uses optimized logic to guess any number chosen by the user between 1 and 100 in the fewest attempts possible.

## 🚀 Features & Concepts Implemented

This project was built to practice core programming fundamentals and computer science concepts:

* **Binary Search Algorithm:** Instead of guessing randomly, the system divides the search space in half with each question, ensuring a maximum of 7 attempts.
* **Control Flow & Loops:** Implements dynamic `while` loops and conditional structures (`if-elif-else`) to handle game states.
* **Input Validation:** Robust error handling to manage invalid user inputs and prevent program crashes.

## 🛠️ Technologies Used

* **Language:** Python 3.x
* **Libraries:** Standard Library only (no external dependencies required)

## 🎮 How to Play

1. Think of a number between 1 and 100.
2. Run the script in your terminal: `python akinator_num.py`
3. Respond to the bot's guesses using the following indicators:
   * `>` if your number is higher.
   * `<` if your number is lower.
   * `=` if the computer guessed your number correctly
