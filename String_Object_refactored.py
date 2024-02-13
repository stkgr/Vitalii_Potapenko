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


# Define function to capitalize only a first letter of the whole text
def capitalize_first_letter(text):
    return text.capitalize()


# Define function to replace iz by is where it is necessary
def fix_iz_is(text):
    return text.replace(' iz ', ' is ')


# Define function to split the whole text to separate words
def split_text(text):
    return text.split(' ')


# Define function to get the last words of the sentences
def get_last_words(text):
    sent_text = ''
    counter = 0
    for word_index in range(0, len(text)):
        # Searching for first word of every sentence
        if text[word_index] not in ['', ' ', '\n'] and counter == 1:
            # Capitalizing the first letter of the first word of every sentence
            text[word_index] = text[word_index].capitalize()
            counter = 0
        # Searching for last word of every sentence
        if text[word_index].endswith(':\n') or text[word_index].endswith('.') or text[word_index].endswith('\n'):
            # Adding the last word to the sentence of the last words
            sent_text += text[word_index]
            counter = 1
    return sent_text.replace('\n', '').replace('.', ' ').replace(':', ' ').replace('  ', ' ').strip() + '.'


# Define function to join all the formatted text and adding an extra sentence
def join_text(text):
    return ' '.join(text).replace("  ", "")


# Define function to count whitespaces in the input text
def count_whitespaces(text):
    return text.count(' ') + text.count('\n') + text.count('\t')


# Call the functions and print the results
text_decapitalize = capitalize_first_letter(input_text)
text_without_iz = fix_iz_is(text_decapitalize)
final_text = split_text(text_without_iz)
text_of_last_words = get_last_words(final_text)
output = join_text(final_text) + ' ' + text_of_last_words
space_count = count_whitespaces(input_text)

print(f'{output} \n\nThe number of whitespace characters in this text is {space_count}.')
