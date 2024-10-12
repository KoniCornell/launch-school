def is_palindrome(string: str):
    '''
    Returns True if string is a palindrome else: False
    A palindrome reads the same forwards and backwards.
    '''
    return string == string[::-1]


def is_real_palindrome(string: str):
    '''
    Similar to is_palindrome(string) However, it is
    case-insensitive and ignores non-alphanumeric chars.
    
    '''
    new_s = [char for char in string if char.isalnum()]
    new_s = ''.join(new_s).casefold()
    return is_palindrome(new_s)

# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)

# case matters
print(is_palindrome('Madam') == False)

# all characters matter
print(is_palindrome("madam i'm adam") == False)


print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True