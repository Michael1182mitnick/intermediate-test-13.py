# Write a program to count the frequency of each word in a given text file.

from collections import defaultdict
import re


def count_word_frequencies(file_path):
    # Create a dictionary to store word frequencies
    word_count = defaultdict(int)

    # Open the file and read it
    with open(file_path, 'r') as file:
        for line in file:
            # Use regular expression to find words
            words = re.findall(r'\b\w+\b', line.lower())

            # Update the word count for each word found
            for word in words:
                word_count[word] += 1

    return word_count


# Example usage
file_path = 'example.txt'  # Replace with the path to your text file
word_frequencies = count_word_frequencies(file_path)

# Print the word frequencies
for word, frequency in word_frequencies.items():
    print(f"'{word}': {frequency}")
