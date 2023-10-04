# Define the input and output file names
input_file_name = "dict.txt"
output_file_name = "5letterwords.txt"

# Function to filter and save 5-letter words
def filter_and_save_5_letter_words(input_file, output_file):
    with open(input_file, "r") as input_file:
        words = [line.strip() for line in input_file if len(line.strip()) == 5]

    words.sort()  # Sort the words alphabetically

    with open(output_file, "w") as output_file:
        for word in words:
            output_file.write(word + "\n")

    print(f"Filtered 5-letter words saved to '{output_file}'.")

# Run the function
filter_and_save_5_letter_words(input_file_name, output_file_name)
