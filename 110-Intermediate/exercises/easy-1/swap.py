def swap(text: str):
    '''
    Swaps the first and last letters of every word in text.
    '''
    new_text = []
    if ' ' in text:
        text = text.split(' ')
        for word in text:
            
            new_text.append(swapper(word))
        new_text = ' '.join(new_text)
    else:
        new_text.append(swapper(text))
        new_text = ''.join(new_text)
         
    return new_text

def swapper(word: str):
    '''
    swaps the first and last letters of word
    '''
    length = len(word)
    if length == 1:
        return word
 
    word = word[-1] + word[1:-1] + word[0]
    return word

            
print(swap('Oh what a wonderful day it is')
      == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
