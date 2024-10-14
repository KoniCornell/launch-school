
# list comprehensions
# [output_expression for item in existing_list if condition]

nums = [1, 2, 3, 4, 5]
squared = [num ** 2 for num in range(1,6)]
print(squared)

even_nums = [num for num in nums if num % 2 == 0]
print(even_nums) 

# set comprehensions
# similar to lists but the output is a set, an unordered collection 
# with no duplicate values

# dictionary expressions
'''
{key_expression: value_expression for item in existing_list
                                  if condition}
'''

fruits = ['apple', 'banana', 'cherry']
fruit_length = {fruit: len(fruit) for fruit in fruits}
print(fruit_length)  # {'apple': 5, 'banana': 6, 'cherry': 6}


# nested lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

flattened_matrix = []

for row in matrix:
    for cell in row:
        flattened_matrix.append(cell)

print(flattened_matrix)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# using comprehension
'''
[output_expression for sublist in outer_list
                   if condition1
                   for item in sublist
                   if condition2] 
'''
new_matrix = [cell for row in matrix
                   for cell in row]
print(new_matrix)


# problem 1 
# Compute and display the total age of the family's male members

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

male_age = [value['age'] for value in munsters.values()
                        if value['gender'] == 'male']

print(sum(male_age))

# problem 2
# return a new list with the same structure, but with the values 
# in each sublist ordered in ascending order

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

sorted_lst = [sorted(element) for element in lst]
print(sorted_lst)

# problem 3
# return a new list with the same structure, but with the
# values in each sublist ordered in ascending order as strings

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

'''
withoout lambda:
sorted_lst = [sorted(sublist, key=str) for sublist in lst]

with lambda below >>> :
'''
sorted_lst = [sorted(sublist, key=lambda element: str(element)) for sublist in lst]
print(sorted_lst)

# Problem 4
# define a dictionary where the key is the first item in each 
# sublist, and the value is the second.

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

# two ways indexing and iterable unpacking
dict1 = {item[0]: item[1] for item in lst}
dict_lst = {key: value for key, value in lst}
print(dict_lst)

# problem 5
# sort the list so that the sub-lists are ordered based on the 
# sum of the odd numbers that they contain. You shouldn't 
# mutate the original list.

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def odd_sum(nums: list):
    return sum([i for i in nums if i % 2 != 0])

new_lst = sorted(lst, key= odd_sum)

print(new_lst)

# problem 6
# return a new list identical in structure to the original but, 
# with each number incremented by 1.

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

new_lst = [{key: value+1 for key, value in element.items()}
                            for element in lst]

print(new_lst)

# problem 7
# return a new list identical in structure to the original, but 
# containing only the numbers that are multiples of 3.
lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

new_lst = [[num for num in element if num % 3 == 0] 
           for element in lst]
print(new_lst)

# problem 8
# return a list that contains the colors of the fruits and the 
# sizes of the vegetables. The sizes should be uppercase, and 
# the colors should be capitalized.

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

grocery_data = [value['size'].upper() if value['type'] == 'vegetable'
                else [item.capitalize() for item in value['colors']] 
                for value in list(dict1.values())
                ]

print(grocery_data)

# Problem 9
# return a list that contains only the dictionaries where 
# all the numbers are even.

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def check_even(element: list):
    # print(element)
    return all([j % 2 == 0 for i in element
                            for j in i])

even_lst = [item for item in lst
                if check_even(list(item.values()))]

# for item in lst:
#     print(list(item.values()))
    

# flat_lst = [[num for num in item.values()] for item in lst]
# print(flat_lst)


print(even_lst)
# print(check_even([2, 3, 6]))