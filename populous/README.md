

# Country Population Guessing Game

Welcome to the Country Population Guessing Game! This Python script allows you to test your knowledge of world populations by guessing the population of various countries in the year 2020. In addition to the guessing challenge, the script provides a visual representation of each country's population history over multiple years.

## How to Play

1. **Installation**: Ensure you have Python installed on your system. You'll also need the Pandas and Matplotlib libraries. You can install them using pip:

   ```bash
   pip install pandas matplotlib
   ```

2. **Data**: The game uses population data from a CSV file named 'world_population.csv'. Make sure this file is in the same directory as the script or provide the correct file path in the code.

3. **Run the Game**: Execute the script using Python:

   ```bash
   python country_population_game.py
   ```

4. **Guess the Population**: The game will randomly select a country and ask you to guess its population in the year 2020. Enter your guess as an integer.

5. **Outcome**: You'll receive feedback on whether your guess is correct or incorrect, along with the actual population figure for the selected country.

6. **Population History**: If available, the script will also display a bar chart showing the population history of the selected country for various years, including 2020 and previous decades.

7. **Play Again**: After each round, you can choose to play again or exit the game.

## Data Source

The population data used in this game is sourced from the 'world_population.csv' file. The CSV file should contain columns for 'Country/Territory', '2020', '2015', '2010', '2000', '1990', '1980', and '1970' representing population figures for these years.

## Acknowledgments

This project was created for educational and entertainment purposes. It provides an engaging way to learn about world populations and test your knowledge.

Enjoy the game and have fun guessing country populations!

