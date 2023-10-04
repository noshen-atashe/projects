import random

# Load the word list
with open("5letterwords.txt", "r") as file:
    word_list = [word.strip() for word in file]

# Choose a random word as the target
target_word = random.choice(word_list)
game_state = ["_" for _ in range(5)]
attempts = 6
guessed_letters = []

print("Welcome to DUMBDLE!")
print("Guess a 5-letter word.\nYou will get 6 attempts")

while attempts > 0:
    guess = input("Enter your guess: ").lower()

    if guess in word_list:
        if guess == target_word:
            print("Congratulations! You guessed the word:", target_word)
            break
        else:
            feedback = []
            for i in range(5):
                if guess[i] == target_word[i]:
                    game_state[i] = guess[i]
                elif guess[i] in target_word:
                    feedback.append(guess[i])

            print(" ".join(game_state))
            if feedback:
                print("Letters in the correct position:", " ".join(game_state))
                print("Letters in the word but in the wrong position:", " ".join(feedback))
    else:
        print("Invalid word. Try again.")
        continue

    guessed_letters.extend(guess)  # Add guessed letters to the list
    unique_guessed_letters = set(guessed_letters)
    incorrect_letters = [letter for letter in unique_guessed_letters if letter not in target_word]

    print("Guessed letters not in the word:", " ".join(incorrect_letters))

    attempts -= 1

if attempts == 0:
    print("You ran out of attempts. The word was:", target_word)
