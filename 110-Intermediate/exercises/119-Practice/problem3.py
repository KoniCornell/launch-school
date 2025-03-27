'''
Pedac:
1. Understanding the problem
    - Input: str
    - Output: str
    - Rules:
        a. Explicit:
            - Takes a string argument
            - Returns a copy of the string
            - Converst every second char of every third
                word converted to uppercase
            - Other chars remain the same
        b. Implicit:
            - 
    - Questions:
        - What if the string is empty?
        - What about special characters?
2. Examples
    original = 'Lorem Ipsum is simply dummy text of the printing world'
    expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
    print(to_weird_case(original) == expected)

    original = 'It is a long established fact that a reader will be distracted'
    expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
    print(to_weird_case(original) == expected)

    print(to_weird_case('aaA bB c') == 'aaA bB c')

    original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
    expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
    print(to_weird_case(original) == expected)

3. Data Structures:
    - list

4. Algorithm:
    - create a list of the words
    - loop through the words
    - mutate only the third word
    - Use a helper function maybe
    - Join the final list
    - return the string
5. Code with intent
'''

def to_weird_case(text: str):
    words = text.split(' ')
    new_words = [weird_case(word) if not (words.index(word) + 1) % 3 
                                    and words.index(word) != 0
                                    else word
                 
                 
                                    for word in words]
    # print(' '.join(new_words))
    return ' '.join(new_words)

def weird_case(string: str):
    new_string = [char.upper() if idx % 2
                  else char
                  for idx, char in enumerate(string)]
    
    return ''.join(new_string)

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)



