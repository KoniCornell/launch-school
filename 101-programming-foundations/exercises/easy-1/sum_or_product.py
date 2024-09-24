'''
calculates the sum or the product of all numbers between 1 and 
the entered integer, inclusive.
'''
number = int(input('Please enter an integer greater than 0: '))
operation = input('Enter "s" to compute the sum, '\
                  'or "p" to compute the product. ')

def compute_sum(num = number):
    total_sum = 0
    for i in range(1,(num + 1)):
        total_sum += i
    return total_sum

# print(sum(10))

def product(num = number):
    total_product = 1
    for i in range(1,(num + 1)):
        total_product *= i
    return total_product

def main():
    match operation:
        case 's':
           total = compute_sum()
           print('The sum of the integers between 1 and'\
                 f'{number} is {total}.')
        case 'p':
           total = product()
           print('The sum of the integers between 1 and'\
                 f'{number} is {total}.')

main()
    