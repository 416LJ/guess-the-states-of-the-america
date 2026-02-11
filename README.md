# Guess the States of the U.S.A.

A fun and interactive game to test your knowledge of U.S. geography, built using Python's `turtle` and `pandas` libraries.

## How to Play

1. **Run the Game**: Execute the `main.py` script.
   ```bash
   python main.py
   ```
2. **Guess a State**: A prompt will appear asking you to enter the name of a U.S. state.
3. **Correct Guesses**: If you guess correctly, the state's name will appear on the map at its correct location.
4. **Winning**: Try to guess all 50 states!
5. **Losing**: You have a limited number of wrong attempts (10 tries). If you run out, the game ends.
6. **Exit**: Type `Exit` in the prompt to quit the game at any time.

## Features

- **Interactive Map**: Uses a visual map of the U.S.
- **Score Tracking**: Keeps track of your correct guesses.
- **Learn from Mistakes**: When you exit or lose, a file named `states_to_learn.csv` is created, listing all the states you missed so you can study them.

## Requirements

- Python 3.x
- `pandas` library

## Installation

1. Clone or download this repository.
2. Install the required library:
   ```bash
   pip install pandas
   ```
3. Ensure the following files are in the same directory:
   - `main.py`
   - `50_states.csv`
   - `blank_states_img.gif`

## Project Structure

- `main.py`: The main game script containing the game logic.
- `50_states.csv`: A CSV file containing the names of all 50 states and their x, y coordinates on the map.
- `blank_states_img.gif`: The background image of the U.S. map.
