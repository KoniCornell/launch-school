def crunch(word: str):
    '''
    takes a string argument and returns a new string that 
    contains the value of the original string with all 
    consecutive duplicate characters collapsed into a 
    single character.
    '''
    try:
        new_word = word[0]
    except IndexError:
        new_word = word
        return word
    j = 0
    for i in range(1, len(word)):
        if new_word[j] == word[i]:
            continue
        j += 1
        new_word += word[i] 

    return new_word
    
# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
