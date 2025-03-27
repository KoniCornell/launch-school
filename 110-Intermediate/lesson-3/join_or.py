def join_or(lst: list, delimiter: str = ', ', last: str = 'or'):
    lst = [str(char) for char in lst]
    last = f'{last} '

    if len(lst) < 1:
        return ''
    
    elif len(lst) == 1:
        return str(*lst)
    
    elif len(lst) == 2:
        return (' '+last).join(lst)
    else:
        string = delimiter.join(lst)
        return ''.join([string[:-1], last, str(string[-1])])

print(join_or([1, 2, 3]))               # => "1, 2, or 3"
print(join_or([1, 2, 3], '; '))         # => "1; 2; or 3"
print(join_or([1, 2, 3], ', ', 'and'))  # => "1, 2, and 3"
print(join_or([]))                      # => ""
print(join_or([5]))                     # => "5"
print(join_or([1, 2]))                  # => "1 or 2"