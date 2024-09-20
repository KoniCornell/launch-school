import random
random_number = random.randint(0, 1)

if random_number == 1:
    print('Yes!')
else:
    print('No!')


'''
A ternary expression is a concise way to choose between two values 
based on some condition. They are often used as an expression 
on the right side of an assignment, as function arguments, 
and as function return values.

Ternary expressions have the following structure:

value1 if condition else value2

'''

print('Yes!' if random_number == 1 else 'No!')