def get_mid_char(sentence):
    '''
    takes a non-empty string argument and returns 
    the middle character(s) of the string.
    '''
    length = len(sentence)

    if length % 2 == 0:
        length = int(length / 2)
        return sentence[(length-1):(length+1)] 
    else:
        return sentence[length//2]
    
print(get_mid_char('I Love Python!!!') == "Py")    # True
print(get_mid_char('Launch School') == " ")        # True
print(get_mid_char('Launchschool') == "hs")        # True
print(get_mid_char('Launch') == "un")              # True
print(get_mid_char('Launch School is #1') == "h")  # True
print(get_mid_char('x') == "x")                    # True