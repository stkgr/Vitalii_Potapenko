# Import the randint and choice functions from the random module
from random import randint, choice as choice

# Create a list of dictionaries
list_of_dict = []
# Create a dictionary to store the result
result = {}
# Create a variable to store the number of dictionaries
number_of_dictionaries = randint(2, 10)

# Create a loop to fill the list with dictionaries
for dictionary in range(number_of_dictionaries):
    # Create a list for adding letters
    list_of_dict.append({})

# Create a loop to fill the dictionaries with random letters and numbers
for dictionary in range(number_of_dictionaries):
    # Create a list of all alphabet letters
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    # Create a variable to store the random number of elements in the dictionary
    number_of_elements = randint(1, len(alphabet))
    # Create a loop to fill the dictionary with random letters and numbers
    for element in range(number_of_elements):
        # Create a variable to store the random letter
        key_value = choice(alphabet)
        # Add the random letter as a key and a random number as a value to the dictionary
        list_of_dict[dictionary][key_value] = randint(0, 100)
        # Remove used letter from the alphabet list
        alphabet.remove(key_value)
# Print the result: random number of dictionaries with random number of elements
print('task 1 result:' + str(list_of_dict))

# Create a dictionary to store the common letters from created dictionaries
common_dict = {}
# Create a loop to fill the common dictionary with the common letters from created dictionaries
for nested_dict in list_of_dict:
    # Create a loop for every letter of every dictionary
    for key_letter in nested_dict:
        # Check if the letter is already in the common dictionary
        if key_letter in common_dict:
            # Check if the value in the current dictionary is greater than the value in the common dictionary
            if nested_dict[key_letter] > common_dict[key_letter]:
                # Update the value of the key letter in the common dictionary with the value from current dictionary
                common_dict.update({key_letter: nested_dict[key_letter]})
        # If the letter is not in the common dictionary
        else:
            # Add the letter and the value to the common dictionary
            common_dict.update({key_letter: nested_dict[key_letter]})


# Set a variable to store the index of the dictionary
dict_index = 0
# Set a variable to store the quantity of the letter
letter_count = 0
# Create a loop to add dictionary indexes to common key letters
for common_letter in common_dict:
    # Set the quantity of the letter to 0
    letter_count = 0
    # Create a loop for every dictionary of the list of dictionaries
    for nested_dict in list_of_dict:
        # Create a loop for every letter of every dictionary
        for key_letter in nested_dict:
            # Check if the letter is the same as the common letter
            if key_letter == common_letter:
                # Increase the quantity of the letter
                letter_count += 1
    # Check if the quantity of the letter is greater than 1
    if letter_count > 1:
        # Create a loop for every dictionary of the list of dictionaries if letter has quantity greater than 1
        for nested_dict in list_of_dict:
            # Increase the index of the dictionary
            dict_index += 1
            # Create a loop for every letter with quantity greater than 1
            for key_letter in nested_dict:
                # Check if the current letter has a value equal to the value of the letter in the common dictionary
                if key_letter == common_letter and nested_dict[key_letter] == common_dict[key_letter]:
                    # Write the key letter with dictionary index and related value to the result dictionary
                    result.update({str(key_letter)+'_'+str(dict_index): nested_dict[key_letter]})
    # If the quantity of the letter is equal to 1
    else:
        # Add the key letter without index and related value to the result dictionary
        result.update({common_letter: common_dict[common_letter]})
    # Reset the index of the dictionary
    dict_index = 0
# Print the result:
# common letters from dictionaries with indexes, if the letter is at least in two dictionaries, and max number values
print('task 2 result:' + str(result))
