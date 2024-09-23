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

FILE_PATH = 'lesson-2/mortgage_prompts.json'

NAN = math.nan
INF = math.inf
CASES = ['0', 0.0, NAN, INF]

with open(FILE_PATH, 'r') as file:
    messages = json.load(file)

def prompt(message):
    print(f"\n==> {message}")

prompt(messages["welcome"])

# check if the input is valid
def invalid_input(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False

def get_loan_amount():
    # get the loan amount
    prompt(messages["loan_amount"])
    #global loan_amount
    loan_amount = input()
    while loan_amount:
        if loan_amount in CASES:
            loan_amount = 0
            break
        while invalid_input(loan_amount):
            prompt(messages["not_valid"])
            loan_amount = input()
        break
    loan_amount = float(loan_amount)
    return loan_amount

def get_apr():
    #global apr
    #get the apr
    prompt(messages["apr"])
    apr = input()

    while apr:
        if apr in {CASES[2], CASES[3]}:
            prompt(messages["not_valid"])
            apr = input()

        elif apr[0] == '-':
            prompt(messages["apr_negative"])
            apr = input()

        else:
            while invalid_input(apr):
                prompt(messages["not_valid"])
                apr = input()
            break

    apr = float(apr)
    return apr

def get_loan_duration():
    #global loan_duration
    #get the loan duration
    prompt(messages["loan_duration"])

    loan_duration = input()

    # handle edge cases for loan duration
    while loan_duration:
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
    #global answer
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

        def get_monthly_payment():
        #global monthly_payment

            try:
                # calculate monthly interest rate
                monthly_rate = apr / 12

                # print(monthly_rate)
                #calcultate monthly_payment
                monthly_payment = loan_amount * \
                   (monthly_rate / (1 - (1 + monthly_rate)**\
                                     (- loan_duration )))
            except ZeroDivisionError:
                monthly_payment = loan_amount / loan_duration

            return monthly_payment

        monthly_payment = get_monthly_payment()

    print(f'\nYour monthly payment is {monthly_payment:.2f}')

def main():
    while True:
        calculation()
        result = another_calculation()

        try:
            result = result.lower()

            if result not in ['y', 'yes']:
                prompt(messages["bye"])
                break
        except (AttributeError, TypeError):
            prompt(messages["bye"])
            break
main()
