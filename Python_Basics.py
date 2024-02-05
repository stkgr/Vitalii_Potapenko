from random import randint

# Creation of a list
numbers_list = []
# Doing the cycle for 100 times
for i in range(100):
    # Adding a random number in range from 0 to 1000 to the list
    numbers_list.append(randint(0, 1000))
# Printing the result list
print(numbers_list)

# # Doing the cycle for every element in the list
for i in range(100):
    # Place max value to the end of the scope of the list that is not sorted
    for j in range(0, len(numbers_list)-i-1):
        # If the current element is bigger than the next one
        if numbers_list[j] > numbers_list[j+1]:
            # Swap the indexes of the elements
            numbers_list[j+1], numbers_list[j] = numbers_list[j], numbers_list[j+1]

# Printing the result list
print(numbers_list)


# Set variable for the sum of even numbers
even_sum = 0
# Set variable for the sum of odd numbers
odd_sum = 0
# Set variable for the count of even numbers
even_count = 0
# Set variable for the count of odd numbers
odd_count = 0

# Doing the cycle for every element in the list
for i in numbers_list:
    # If the number is even
    if i % 2 == 0:
        # Add the number to the sum of even numbers
        even_sum += i
        # Increase the count of even numbers
        even_count += 1
    # If the number is odd
    else:
        # Add the number to the sum of odd numbers
        odd_sum += i
        # Increase the count of odd numbers
        odd_count += 1

# Print the average of even and odd numbers in two lines
print('Average of even numbers:' + str(even_sum/even_count), 'Average of odd numbers:' + str(odd_sum/odd_count), sep='\n')
