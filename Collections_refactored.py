from random import randint, choice


# Define a function to create a random number of dictionaries in range from 2 to 10
def create_list_of_dictionaries():
    list_of_dict = []
    number_of_dictionaries = randint(2, 10)
    for dictionary in range(number_of_dictionaries):
        list_of_dict.append({})
    return list_of_dict


# Define a function to fill the dictionaries with random letters and numbers
def fill_dictionaries(list_of_dict):
    # Create a loop to fill every dictionary with random letters and numbers
    for dictionary in list_of_dict:
        # Set the range of values for keys and values
        alphabet = list("abcdefghijklmnopqrstuvwxyz")
        number_of_elements = randint(1, len(alphabet))
        # Set the values for the keys
        for element in range(number_of_elements):
            key_value = choice(alphabet)
            dictionary[key_value] = randint(0, 100)
            # Remove the used letter from the alphabet list
            alphabet.remove(key_value)
    return list_of_dict


# Define a function to find common letters in the dictionaries
def find_common_letters(list_of_dict):
    common_dict = {}
    for nested_dict in list_of_dict:
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
    return common_dict


# Define a function to create a dictionary with common letters and their values
def create_result_dictionary(common_dict, list_of_dict):
    result = {}
    for common_letter in common_dict:
        letter_count = 0
        dict_index = 0
        for nested_dict in list_of_dict:
            for key_letter in nested_dict:
                # Check if the letter of the current dictionary is in the common dictionary
                if key_letter == common_letter:
                    # Increase the quantity of the letter
                    letter_count += 1
        # Check if the letter is in more than one dictionary
        if letter_count > 1:
            for nested_dict in list_of_dict:
                # Increase the index of the dictionary
                dict_index += 1
                for key_letter in nested_dict:
                    # Check if the common dictionary has the key from the current dictionary and if the values are equal
                    if key_letter == common_letter and nested_dict[key_letter] == common_dict[key_letter]:
                        # Add the key with dictionary number and the value to the result dictionary
                        result.update({str(key_letter)+'_'+str(dict_index): nested_dict[key_letter]})
        # If the letter is in only one dictionary
        else:
            # Add the key without the dictionary number and the value to the result dictionary
            result.update({common_letter: common_dict[common_letter]})
    return result


# Define a function to print the results both of the tasks
def print_task_results(list_of_dict, result):
    print('task 1 result:', list_of_dict)
    print('task 2 result:', result)


# Call the functions to execute the tasks
list_of_dicts = create_list_of_dictionaries()
list_of_dicts = fill_dictionaries(list_of_dicts)
dict_of_common_keys = find_common_letters(list_of_dicts)
result_dict = create_result_dictionary(dict_of_common_keys, list_of_dicts)
print_task_results(list_of_dicts, result_dict)
