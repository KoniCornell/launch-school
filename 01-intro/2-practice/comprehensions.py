'''
Comprehensions don't build their results all at once. 
Each kind of comprehension works something like this:

result = empty_collection               # [], {}, set()
for item in collection:
    result.append(item)

'''
# format for list comprehensions

# [ expression for element in iterable if condition ]

# Examples (used triple quotes for multi-line comments)
'''
Here, we're iterating over the numbers in the indicated range: 0, 1, 2, 3, 4. 
We compute the square with number * number for each number. 
Finally, Python collects all the squares into a list and assigns 
the list to the squares variable. Voila! We now have a list of squares.

'''

squares = [ number * number for number in range(5)]
print(squares)

multiples_of_6 = [ number for number in range(20)
                   if number % 6 == 0 ]
print(multiples_of_6)      # [0, 6, 12, 18]

# list comprehensions in dict with multiple conditions
cats_colors = {
    'Tess':   'brown',
    'Leo':    'orange',
    'Fluffy': 'gray',
    'Ben':    'black',
    'Kat':    'orange',
}

names = [ name.upper()
          for name in cats_colors
          if cats_colors[name] == 'orange'
          if name[0] == 'L' ]
print(names) # ['LEO']


'''
Dictionary comprehensions are almost identical to list comprehensions. 
However, they create new dictionaries instead of lists.
'''

# format for dictionary comprehensions
# { key: value for element in iterable if condition }

squares = { f'{number}-squared': number * number
            for number in range(1, 6) }
print(squares)
# pretty-printed for clarity.
{
    '1-squared': 1,
    '2-squared': 4,
    '3-squared': 9,
    '4-squared': 16,
    '5-squared': 25
}