# Function to load the current words from the file into a list
def load_words(file_name):
    words = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                word = line.strip()
                if len(word) == 5:
                    words.append(word)
    except FileNotFoundError:
        pass
    return words

# Function to save the words from the list back to the file alphabetically
def save_words(file_name, words):
    words.sort()
    with open(file_name, "w") as file:
        for word in words:
            file.write(word + "\n")

# Main function
def main():
    file_name = "5letterwords.txt"
    words_list = load_words(file_name)

    print("Welcome to the 5-Letter Word Editor!")
    while True:
        print("\nOptions:")
        print("1. Add a 5-letter word")
        print("2. Remove a 5-letter word")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            word_to_add = input("Enter the 5-letter word you want to add: ").strip().lower()
            if len(word_to_add) == 5 and word_to_add not in words_list:
                words_list.append(word_to_add)
                save_words(file_name, words_list)
                print(f"'{word_to_add}' has been added to the dictionary.")
            else:
                print("Invalid input or word already exists in the dictionary.")
        elif choice == "2":
            word_to_remove = input("Enter the 5-letter word you want to remove: ").strip().lower()
            if word_to_remove in words_list:
                words_list.remove(word_to_remove)
                save_words(file_name, words_list)
                print(f"'{word_to_remove}' has been removed from the dictionary.")
            else:
                print("Word not found in the dictionary.")
        elif choice == "3":
            print("Exiting the Word Editor. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3).")

if __name__ == "__main__":
    main()
