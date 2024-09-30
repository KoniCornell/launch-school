# Question 1
# Write two distinct ways of reversing the list 
# without mutating the original list.

numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

reversed_numbers = numbers[::-1]
reversed_numbers = list(reversed(numbers))

# Question 2
# determine whether the number is included in the list.
numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

print(number1 in numbers)
print(number2 in numbers)

# Question 3
# determine whether 42 lies between 10 and 100
print(42 in range(10,101))
print(100 in range(10,101))
print(101 in range(10,101))

# Question 4
# mutate the list by removing the number at index 2
numbers = [1, 2, 3, 4, 5]
# del numbers[2]
numbers.pop(2)
print(numbers)

# Question 5
# check if they are of type list
numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

isinstance(numbers, list)  # True
isinstance(table, list)    # False

# type(numbers) is list      # True
# type(table) is list        # False

# Question 6
title = "Flintstone Family Members"
centered_title = title.center(40)
# print(' '* 20, title)
print(centered_title)

# Question 7
# count the number of lower-case t 
statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

print(statement1.count('t'))
print(statement2.count('t'))
