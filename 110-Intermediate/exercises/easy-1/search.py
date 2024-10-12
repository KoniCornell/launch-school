num1 = int(input('Enter the 1st number: '))
num2 = int(input('Enter the 2nd number: '))
num3 = int(input('Enter the 3rd number: '))
num4 = int(input('Enter the 4th number: '))
num5 = int(input('Enter the 5th number: '))
num6 = int(input('Enter the last number: '))

numbers = [num1, num2, num3, num4, num5]

if num6 in numbers:
    print(f'{num6} is in {num1},{num2},{num3},{num4},{num5}')
else:
    print(f"{num6} isn't in {num1},{num2},{num3},{num4},{num5}")