# problem 1 : demonstrate how you would access the letter g 

lst1 = ['a', 'b', ['c', ['d', 'e', 'f', 'g']]]
print(lst1[2][1][3])

lst2 = [
    {
        'first': ['a', 'b', 'c'],
        'second': ['d', 'e', 'f']
    },
    {
        'third': ['g', 'h', 'i']
    }
]
print(lst2[1]['third'][0])

lst3 = [['abc'], ['def'], {'third': ['ghi']}]
print(lst3[2]['third'][0][0])

dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}
print(dict1['b'][1])

# This one is much more challenging than it looks! Try it, but don't
# stress about it. If you don't solve it in 10 minutes, you can look
# at the answer.
dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, 'f': 1}, '3rd': {'g': 0}}
print(list(dict2['3rd'].keys())[0])

# problem 2
'''
demonstrate how you would change the value 3 to 4
'''

lst1 = [1, [2, 3], 4]
lst1[1][1] = 4
print(lst1)

lst2 = [{'a': 1}, {'b': 2, 'c': [7, 6, 5], 'd': 4}, 3]
lst2[2] = 4
print(lst2)

dict1 = {'first': [1, 2, [3]]}
dict1['first'][2][0] = 4
print(dict1)

dict2 = {'a': {'a': ['1', 'two', 3], 'b': 4}, 'b': 5}
dict2['a']['a'][2] = 4
print(dict2)

# propblem 3
a = 2
b = [5, 8]
lst = [a, b]

lst[0] += 2
lst[1][0] -= a

'''
The value of a didn't change since we don't reference a at any point. 
The code lst[0] += 2 modifies the list lst, but not a. In effect, 
we are assigning a new value to that index of the list so that instead 
of lst[0] containing 2, the value obtained from a, it now contains 4.
'''

# problem 4
'''
Given the object shown below, print the name, age, and gender 
of each family member:
'''

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

for key, value in munsters.items():
    print(f'{key} is a {value['age']}-year-old {value['gender']}.')