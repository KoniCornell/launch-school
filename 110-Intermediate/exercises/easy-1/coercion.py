
def string_to_integer(string):

    result = 0
    dict_string = {str(num): num for num in range(0, 10)} 

    for num in string:
        int_num = dict_string[num]
        result = (10 * result) + int_num

    return result 

def string_to_signed_integer(string):
    match string[0]:
        case '-':
            return -string_to_integer(string[1:])
        case '+':
            return string_to_integer(string[1:])
        case _:
            return string_to_integer(string)   

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(number):
    result = ''

    while number > 0:
        number, remainder = divmod(number, 10)
        result = DIGITS[remainder] + result

    return result or '0'

def signed_integer_to_string(number):
    if number < 0:
        return f"-{integer_to_string(-number)}"
    elif number > 0:
        return f"+{integer_to_string(number)}"
    else:
        return "0"
    

print(string_to_integer("4321") == 4321)  # True
print(string_to_integer("570") == 570)    # True