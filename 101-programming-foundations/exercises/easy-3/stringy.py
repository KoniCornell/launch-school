def stringy(num: int):
    binary_str = ''
    for i in range(num):
        binary_str += '1' if i % 2 == 0 else '0'
    return binary_str
    

# Tests 
print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True