import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data from the 'world_population.csv' file
df = pd.read_csv('world_population.csv')

# Define the column titles for the population history years
population_years = ['2022', '2020', '2015', '2010', '2000', '1990', '1980', '1970']

def main():
    print("Welcome to the 'Guess the Country's Population' game!")
    while True:
        country_row = df.sample()
        country_name = country_row['Country/Territory'].values[0]
        actual_population = country_row['2020'].values[0]

        print(f"Guess the population of {country_name} in the year 2020:")

        try:
            guess = int(input("Enter your guess: "))

            if guess == actual_population:
                print("Congratulations! Your guess is correct.")
            else:
                print(f"Sorry, your guess is incorrect. The population of {country_name} in 2020 was {actual_population}.")

            # Plot population history (if available)
            population_history = country_row[population_years].values.flatten()
            plt.bar(population_years, population_history)
            plt.xlabel('Year')
            plt.ylabel('Population')
            plt.title(f'Population History of {country_name}')
            plt.show()

        except ValueError:
            print("Invalid input. Please enter a valid integer guess.")

        play_again = input("Play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
