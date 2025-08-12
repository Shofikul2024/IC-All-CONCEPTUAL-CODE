# github err kono help lagle  : git help -a

# aita likhle  onk command  diye help kporbe github


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/













# --------------------------------------------
# String Case Transformations
# --------------------------------------------

full_name = "shamim dfdgsfgghsfghh stwertrtwer wertwert"
print("Uppercase:", full_name.upper())  # Convert entire string to uppercase

user_name = "SABBIR"
print("Lowercase:", user_name.lower())  # Convert entire string to lowercase

sentence = "i love python."
print("Capitalized:", sentence.capitalize())  # Capitalize only the first letter

long_name = "shamim azad  ajfalkl dhafajf asdfadjf adjfadjf asfadfj"
print("Title Case:", long_name.title())  # Capitalize first letter of each word

mixed_case_text = "pyThoN"
print("Swapcase:", mixed_case_text.swapcase())  # Swap uppercase to lowercase and vice versa

# --------------------------------------------
# Whitespace Handling and Validation
# --------------------------------------------

email_with_spaces = "                shamim@email.com  "
print("Right Stripped Email:", email_with_spaces.rstrip())  # Remove trailing whitespaces

numeric_string = "23798234"
print("Is Digits?:", numeric_string.isdigit())  # Check if string contains only digits

alphabetic_text = "python"
print("Is Alphabetic?:", alphabetic_text.isalpha())  # Check if string contains only letters

lowercase_text = "python"
print("Is Lowercase?:", lowercase_text.islower())  # Check if all characters are lowercase

uppercase_text = "PYTHON"
print("Is Uppercase?:", uppercase_text.isupper())  # Check if all characters are uppercase

space_string = " "
print("Is Whitespace Only?:", space_string.isspace())  # Check if string contains only whitespace

title_text = "Python Fundamentals"
print("Is Title Case?:", title_text.istitle())  # Check if string is title-cased

# --------------------------------------------
# Replacing and Splitting Strings
# --------------------------------------------

tech_text = "I love JavaScript"
print("Replaced Text:", tech_text.replace("JavaScript", "Python"))  # Replace substring

sample_text = "Lorem Ipsum is simply dummy"
word_list = sample_text.split(" ")  # Split string into list by spaces
print("Word List:", word_list)
print("Word Count:", len(word_list))

multiline_text = """It is a long established fact
that a reader will be distracted by
the readable content of a page when looking at its layout."""
line_list = multiline_text.splitlines()  # Split string into lines
print("Line List:", line_list)

# --------------------------------------------
# Joining List into String
# --------------------------------------------

words = ["Bangladesh", "is", "a", "beautiful", "country."]
sentence = " ".join(words)  # Join list into sentence
print("Joined Sentence:", sentence)

# --------------------------------------------
# Startswith and Endswith
# --------------------------------------------

country_sentence = "Bangladesh is a beautiful country."
print("Starts with 'Bangladesh is'?:", country_sentence.startswith("Bangladesh is"))
print("Ends with 'country.'?:", country_sentence.endswith("country."))

phone_number = "+8801711111111"
print("Is Bangladeshi Number?:", phone_number.startswith("+880"))

email_address = "shamimazad@gmail.com"
print("Is Gmail?:", email_address.endswith("@gmail.com"))
print("Is Outlook?:", email_address.endswith("@outlook.com"))

# --------------------------------------------
# Finding and Counting Substrings
# --------------------------------------------

country_list_text = "China Thailand Bangladesh Bhutan Bangladesh Bangladesh"

# Safe search using find (returns -1 if not found)
not_found_index = country_list_text.find("Bangladeshi")
print("Index of 'Bangladeshi' (using find):", not_found_index)

# Right-most occurrence of substring
last_index = country_list_text.rfind("Bangladesh")
print("Last Occurrence of 'Bangladesh':", last_index)

# index search(raises ValueError if not found)
# found_index = country_list_text.index("Bangladeshi")
# print("Index of 'Bangladeshi' (using index):", found_index)

# Count occurrences of substring
bangladesh_count = country_list_text.count("Bangladesh")
print("Number of times 'Bangladesh' appears:", bangladesh_count)
