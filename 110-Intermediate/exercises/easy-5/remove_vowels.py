def remove_vowels(lst: list):
    new_lst = []
    for word in lst:
        new_word = ''
        for char in word:
            if char.lower() not in 'aeiou':
                new_word += char 
        new_lst.append(new_word)
    return new_lst



# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True