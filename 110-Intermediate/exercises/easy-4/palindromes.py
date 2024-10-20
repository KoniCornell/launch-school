def substrings(lst: list):
    
    result = [lst[j:i + 1] 
            for j in range(len(lst))
            for i in range(j, len(lst))]
    # print(result)
    
    return result

def palindromes(text: list):
    text = substrings(text)
    result = [string 
            for string in text
            if string == string[::-1] and len(string) > 1]
    print(result)
    return [string 
            for string in text
            if string == string[::-1] and len(string) > 1]

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True