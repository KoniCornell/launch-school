def penultimate(sentence):
    '''
    returns the next to last word in the string argument
    '''
    sentence = sentence.split(' ')
    return sentence[-2]

# These examples should print True
print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")