age = int(input('What is your age? '))
print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')

print()

#using a for loop
# Note that range does not include the stop.

print(f'You are {age} years old.')
print()

for i in range(10,50,10):
    print(f'In {i} years, you will be {age + i} years old.')
    #print(i)