'''
mortgage calculator that determines the monthly payment assuming that
interest is compounded monthly.

'''
# constants
# welcome prompt
# Ask the user for the following
    # the loan amount
    # the Annual Percentage Rate (APR) *(let the input be 5 for 5%)*
    # the loan duration in months.

# calculate
    # monthly interest rate (APR / 12)
    # loan duration in months

# *remember it is compunded monthly*

# m = p * (j / (1 - (1 + j) ** (-n)))
# m = monthly payment
# p = loan amount
# j = monthly interest rate
# n = loan duration in months

# once done create a json for the prompts.
# wrap everthing in functions
# call main
# voila!

import json
import math
import os

FILE_PATH = 'lesson-2/mortgage_prompts.json'

NAN = math.nan
INF = math.inf
CASES = [NAN, INF, None, '', '0']

with open(FILE_PATH, 'r') as file:
    messages = json.load(file)

def prompt(message):
    print(f"\n==> {message}")

prompt(messages["welcome"])

# check if the input is valid
def invalid_input(number_str):
    try:
        if (number_str in CASES) or (number_str[0] == '-'):
            return True
        float(number_str)
    except ValueError:
        return True
    return False

def get_loan_amount():
    # get the loan amount
    prompt(messages["loan_amount"])
    loan_amount = input()
    while invalid_input(loan_amount):
        prompt(messages["not_valid"])
        loan_amount = input()
    loan_amount = float(loan_amount)
    return loan_amount

def get_apr():
    #get the apr
    prompt(messages["apr"])
    apr = input()

    while True:
        if apr == '0':
            break
        while invalid_input(apr):
            prompt(messages["not_valid"])
            apr = input()
        break

    apr = float(apr)
    return apr

def get_loan_duration():
    #get the loan duration
    prompt(messages["loan_duration"])

    loan_duration = input()

    # handle edge cases for loan duration
    while True:
        if loan_duration in CASES:
            prompt(messages["loan_duration_zero"])
            loan_duration = input()
        else:
            while invalid_input(loan_duration):
                prompt(messages["not_valid"])
                loan_duration = input()
            break
    loan_duration = float(loan_duration)

    return loan_duration

def another_calculation():
    prompt(messages["another_calculation"])
    answer = input()
    return answer

def calculation():
    loan_amount = get_loan_amount()
    if loan_amount == 0:
        monthly_payment = 0.00

    else:
        apr = get_apr()
        loan_duration = get_loan_duration()
        try:
            # calculate monthly interest rate
            monthly_rate = (apr / 100) / 12
            #calcultate monthly_payment
            monthly_payment = loan_amount * \
                (monthly_rate / (1 - (1 + monthly_rate)**\
                                    (- loan_duration )))
        except ZeroDivisionError:
            monthly_payment = loan_amount / loan_duration

    print(f'\nYour monthly payment is {monthly_payment:.2f}')

def again(choice):
    while True:
        try:
            choice = choice.lower()

        except (AttributeError, TypeError):
            prompt(messages["repeat"])
            choice = another_calculation()

        if choice not in ['y', 'yes', 'n', 'no']:
            prompt(messages["repeat"])
            choice = another_calculation()
        elif choice in ['n', 'no']:
            prompt(messages["bye"])
            return False
        else:
            console_clear()
            return True

def console_clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    loop = True
    while loop:
        calculation()
        result = another_calculation()
        loop = again(result)

main()