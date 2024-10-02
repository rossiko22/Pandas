# Example Text Manipulation

# Initial text
text = "Hello World"

# Convert text to lowercase and uppercase
lower_text = text.lower()
upper_text = text.upper()

# List of strings to join
list_to_join = ['1', '2', '3', '12', '13', '231']

# Text with items to clean and manipulate
text_to_clean = "banana, melon, watermelon, melson"

# Filename example
filename = "list.csv"

# Multiline text
multiline_text = "Line 1\n Line2\n Line3\n"

# Split text by commas
splitted_text = text_to_clean.split(",")

# Strip specified characters from the edges of the text
stripped_text = text_to_clean.strip("!d")  # Note: strips any combination of '!', 'd', and spaces from edges

# Replace "ban" with "tan" in the text
replaced_text = text_to_clean.replace("ban", "tan")

# Join list elements into a single string separated by slashes
joined_text = "/".join(list_to_join)

# Check if the filename ends with ".csv"
suffix_prefix = filename.endswith(".csv")

# Filter items in the list that start with "1"
starts_with_from_list = [item for item in list_to_join if item.startswith("1")]

# Find the index of the first occurrence of "mel" in the text
find_string = text_to_clean.find("mel")

# Convert filtered digit strings to integers
check_if_digit = [int(item) for item in list_to_join if item.isdigit()]

# Split multiline text into individual lines
splitted_multiline_text = multiline_text.splitlines()

# Print results
print(f"Splitted Text: {splitted_text}")
print(f"Stripped Text: {stripped_text}")
print(f"Replaced Text: {replaced_text}")
print(f"Joined Text: {joined_text}")
print(f"Suffix Prefix: {suffix_prefix}")
print(f"Starts With: {starts_with_from_list}")
print(f"Found Text: {find_string}")
print(f"Is Digit Check: {check_if_digit}")
print(f"Splitted Multiline Text: {splitted_multiline_text}")
print(f"Upper Text: {upper_text} Lower Text: {lower_text}")

# Essential Built-in Functions in Python

# Read input from the user
stdin = input("Enter your number: ")

# Find the length of the input string
length = len(stdin)

# Convert characters to their ASCII values
from_characters_to_ascii = [ord(item) for item in stdin]

# Convert ASCII values back to characters
from_ascii_to_character = [chr(item) for item in from_characters_to_ascii]

# Print results
print(f"From Characters to ASCII: {from_characters_to_ascii}")
print(f"From ASCII to Characters: {from_ascii_to_character}")
