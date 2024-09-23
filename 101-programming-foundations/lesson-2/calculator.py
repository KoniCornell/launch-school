
# Ask the user for the first number
# Ask the user for the second number
# Ask the user for an operation to perform
# Perform the operation on the two numbers
# Print the result to the terminal

import json

#import os

#print(os.getcwd())

file_path = 'lesson-2/calculator_prompts.json'

with open(file_path, 'r') as file:
    messages = json.load(file)

# print('hi')

def prompt(message):
    print(f"==> {message}")



def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def get_numbers():

    # Ask the user for the first number
    prompt(messages["number1"])
    global number1 
    number1 = input()

    while invalid_number(number1):
        prompt(messages["not_valid"])
        number1 = input()

    # Ask the user for the second number
    prompt(messages["number2"])
    global number2
    number2 = input()

    while invalid_number(number2):
        prompt(messages["not_valid"])
        number2 = input()

    
    number1 = float(number1)
    number2 = float(number2)

    return number1, number2



def do_operation():
    # Ask the user for an operation to perform
    print(messages["operation_question"])
    print(messages["operation_sign"])
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(messages["valid_operation"])
        operation = input()

    match operation:

        case '1':
            output = number1 + number2
        case '2':
            output = number1 - number2
        case '3':
            output = number1 * number2
        case '4':
            output = number1 / number2

    print(f'The result is: {output}')

def new_calculation():
    prompt(messages["new_calculation"])
    global answer
    answer = input()
    
    

def main():
    prompt(messages["welcome"])
    number1, number2 = get_numbers()
    print(f'{number1} {number2}')
    do_operation()
    new_calculation()


while True:

    main()

    if answer != 'y':
        break