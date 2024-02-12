# Set a variable with input text
input_text = 'homEwork:\n  ' \
             'tHis iz your homeWork, copy these Text to variable.\n\n  ' \
             '' \
             'You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE ' \
             'senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.' \
             '' \
             '\n\n  it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.\n\n  ' \
             '' \
             'last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ' \
             'ALL whitespaces. I got 87.'


# Capitalizing only a first letter of the whole text
text_decapitalize = input_text.capitalize()
# Replacing iz by is where it is necessary
text_without_iz = text_decapitalize.replace(' iz ', ' is ')
# Splitting the whole text to separate words
text = text_without_iz.split(' ')


# Creating empty variable to store the last words of the sentences
sent_text = ''
# Creating a counter to check if the word is the first or the last word of the sentence
counter = 0


# Loop for every word of the text
for word_index in range(0, len(text)):
    # Creating a variable to store the current word
    word = text[word_index]
    # Searching for first word of every sentence
    if text[word_index] not in ['', ' ', '\n'] and counter == 1:
        # Capitalizing the first letter of the word
        text[word_index] = text[word_index].capitalize()
        # Resetting the counter
        counter = 0
    # Searching for last word of every sentence
    if text[word_index].endswith(':\n') or text[word_index].endswith('.') or text[word_index].endswith('\n'):
        # Adding the last word to the variable
        sent_text += text[word_index]
        # Setting the counter to 1
        counter = 1

# Formatting the result sentence of all the last words
sent_text = sent_text.replace('\n', '').replace('.', ' ').replace(':', ' ').replace('  ', ' ').strip() + '.'

# Join all the formatted text and adding an extra sentence
output = ' '.join(text).replace("  ", "") + ' ' + sent_text

# Counting whitespaces in the input text
space_count = input_text.count(' ') + input_text.count('\n') + input_text.count('\t')

# Printing the results
print(f'{output} \n\nThe number of whitespace characters in this text is {space_count}.')
