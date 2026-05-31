# 🎲 NUMBER GUESSING GAME
### *An Interactive, Terminal-Based Logic Game*

Welcome to the Number Guessing Game—a lightweight, interactive Python application designed to challenge your deductive skills against an automated dealer. 

---

## 💻 What is This Project?
This is a clean, terminal-based game built in Python where the script dynamically generates a secret number within a specified range (0 to 10). The user has a limited number of attempts to guess the correct number, receiving real-time hint telemetry after each attempt.

---

## 🚀 Key Features & Capabilities

*   **Dynamic Hint Engine:** Automatically evaluates your input and provides instant feedback (`too high` or `too low`) to help you narrow down the target.
*   **Built-in Input Validation:** Micro-managed error handling ensures that accidental text inputs or typos don't break the application or cost you a turn.
*   **Turn-Limit Constraint:** Adds a layer of difficulty by capping your maximum attempts at **5 guesses** before the game terminates and reveals the answer.
*   **Score Tracking:** Automatically logs and displays your total number of attempts upon completion, differentiating between single and plural guess achievements.

---

## ⏱️ How to Play (In 2 Simple Steps)

Launch the script and let the game handle the logic.

1. **Start the Game:** Run the script in your terminal. The system will select a secret number between 0 and 10.
2. **Submit Your Guesses:** Type your guess and press `Enter`. Use the feedback to adjust your next move.

> **Note:** If you fail to guess the number within **5 attempts**, the script will automatically end the game and reveal the correct number.

---

## 🛠️ Prerequisites & Installation

No external dependencies or `pip` installations are required. This project runs entirely on standard built-in Python libraries.

1. Ensure you have **Python 3.x** installed.
2. Clone or download the script file named `guess_the_num.py`.
3. Run the script via your terminal:
```bash
   python guess_the_num.py
