
# Function that returns True if argument's absolute value is odd
# otherwise False


def odd_absolutely(number):
    if number < 0:
        return -(number) % 2 != 0
    else:
        return number % 2 != 0
    
# simpler solution is to use abs()    
# print(abs(-1))


print(odd_absolutely(-3))
print(odd_absolutely(0))
print(odd_absolutely(1))
print(odd_absolutely(2))


'''
def odd(number):
    return abs(number) % 2 != 0


print(odd(5))
'''


