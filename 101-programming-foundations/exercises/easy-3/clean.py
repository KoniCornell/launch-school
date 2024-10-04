def clean_up(word: str):
    clean_word = ''
    alpha_list = list(range(65,91)) + list(range(97,123))
    for char in word:
        if ord(char) not in alpha_list:
            try:
                if len(clean_word) < 1:
                    clean_word += ' '
                    continue

                clean_word += ' ' if clean_word[-1] != ' ' else ''

            except IndexError:
                continue
        else:
            clean_word += char

    return clean_word

'''def clean_up(text):
    clean_text = ''

    for idx, char in enumerate(text):
        if char.isalpha():
            clean_text += char
        elif idx == 0 or clean_text[-1] != ' ':
            clean_text += ' '

    return clean_text'''

# ord(a) = 97
# ord('Z') = 90

print(clean_up('---wh [ [ ]] helo p'))
print(clean_up("---what's my +*& line?") == " what s my line ")
# True