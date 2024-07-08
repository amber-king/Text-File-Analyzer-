import getpass  # Optional: For hidden user input


def count_words(text):
    """Counts the number of words in the provided text."""
     # Split the text into words (handling whitespace characters)
    words = text.split()
    word_count = len(words)  # Count the number of words in the list
    return word_count  # Replace 'word_count' with the actual calculated count

def count_characters(text):
    """Counts the number of characters in the provided text."""
    char_count = len(text)  # Count the length of the text string (number of characters)
    return char_count  # Replace 'char_count' with the actual calculated count

def count_lines(text):
    """Counts the number of lines in the provided text."""
    # Split the text by newline characters
    lines = text.splitlines()
    line_count = len(lines)  # Count the number of lines
    return line_count  # Replace 'line_count' with the actual calculated count

def find_word_count(text, word):
    """Counts the number of occurrences of a specific word in the provided text."""
    # Split the text into words (handling whitespace characters)
    words = text.split()
    count = 0
    for w in words:
        # Convert both word and text to lowercase for case-insensitive search (optional)
        if word.lower() == w.lower():  # Adjust for case sensitivity if needed
            count += 1
    return count


# Open the text file
with open("textreader.py", "r") as file:
    text = file.read()

# Optional: Hide user input (e.g., for sensitive words)
# search_word = getpass.getpass("Enter the word to search for (hidden): ")

search_word = input("Enter the word to search for: ")

# Call the analysis functions
word_count = count_words(text)
char_count = count_characters(text)
line_count = count_lines(text)
specific_word_count = find_word_count(text, search_word)

# Print the results
print("Word Count:", word_count)
print("Character Count:", char_count)
print("Line Count:", line_count)
print("Specific Word Count ('", search_word, "'):", specific_word_count)
