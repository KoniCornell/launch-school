def clean_word(text: str):
    '''
    returns text with only alphanumeric chars
    '''
    text = text.split()
    new_text = []
    for word in text:
        new_word = [letter 
                     for letter in word 
                     if letter.isalnum()]
        new_text.append(''.join(new_word))
    
    new_text = ' '.join(new_text)
    return new_text


def word_sizes(text: str):
    '''
    returns a dictionary that shows the number of words 
    of different sizes.
    ''' 
    new_text = clean_word(text)       
    words_len_count = {}
    words_len = [len(word) for word in new_text.split()]


    for i in words_len:
        if i == 0:
            return words_len_count
        words_len_count[i] = words_len.count(i)
    
    return words_len_count


# All of these examples should print True


string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 2, 3: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 3})

string = 'Humpty Dumpty sat on a w@ll'
print(word_sizes(string) == {6: 2, 3: 2, 2: 1, 1: 1})

string = "What's up doc?"
print(word_sizes(string) == {5: 1, 2: 1, 3: 1})

print(word_sizes('') == {})



