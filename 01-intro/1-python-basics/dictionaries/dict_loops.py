'''

    .keys() returns the keys through a dict_keys object.
    .values() returns the values through a dict_values object.
    .items() returns both the keys and values through a dict_items object.

    .get() method to access a dictionary value if it exists. Returns None if absent.
    You can also specify a message like 
    print(dict.get('name', 'name not found!'))

    .pop() method removes and returns an item based on a given key.
    .popitem() method removes the last item in a dictionary and returns it.

     del() method removes an item based on a given key. del numbers['high']


'''




numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for key, value in numbers.items():
    print(f'A {key} number is {value}.')