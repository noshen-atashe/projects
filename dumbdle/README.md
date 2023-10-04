# Dumbdle - A Wordle-inspired Word Guessing Game

Dumbdle is a simple and entertaining word guessing game that challenges players to guess a hidden 5-letter word. The game provides clues about which letters are in the correct position and which letters are correct but in the wrong position. Test your wordplay skills and enjoy hours of fun!

## How to Play

### Prerequisites
- Ensure you have Python installed on your computer.

### Getting Started
1. Clone this repository to your local machine.

   ```bash
   git clone https://github.com/noshen-atashe/dumbdle.git


2. Navigate to the project folder.

   ```bash
   cd dumbdle
   ```

3. Run the game by executing the following command:

   ```bash
   python dumbdle.py
   ```

### Gameplay
- The game starts with a hidden 5-letter word represented by underscores, like this: `_ _ _ _ _`.
- Your goal is to guess the word correctly within a limited number of attempts.
- Enter a 5-letter word as your guess.
- The game will provide feedback:
  - Letters in the correct position are shown in uppercase (e.g., `A _ _ _ _`).
  - Correct letters in the wrong position are shown in lowercase (e.g., `a _ _ _ _`).
  - Incorrect letters are displayed as underscores (e.g., `_ _ _ _ _`).

### Dictionary Management
- The game uses a filtered dictionary of 5-letter words to choose the hidden word.
- The filtered dictionary is stored in the '5letterwords.txt' file.
- You can manage the filtered dictionary using the following scripts:

#### Filter the Dictionary
- `makeDict.py`: Filters the full dictionary ('dict.txt') for 5-letter words and stores them in '5letterwords.txt'.

   ```bash
   python makeDict.py
   ```

#### Edit the Filtered Dictionary
- `editDictionary.py`: Allows you to add or remove 5-letter words from '5letterwords.txt'.

   ```bash
   python editDictionary.py
   ```

## Files in the Repository

- `dumbdle.py`: The main game file.
- `makeDict.py`: Code to filter the full dictionary and create '5letterwords.txt'.
- `editDictionary.py`: Script for adding or removing words from '5letterwords.txt'.
- `dict.txt`: The full dictionary of all words.
- `5letterwords.txt`: The filtered dictionary (make sure to keep this file updated).

## Acknowledgments

Dumbdle is inspired by the popular word game Wordle. It was created for educational and entertainment purposes.

Enjoy playing Dumbdle, and may your word-guessing skills sharpen as you go!

