def keep_keys(colours: dict, colours_keys: list):
    return {colours_keys[idx]: colours[key]
             for idx, key in enumerate(colours_keys)}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True
