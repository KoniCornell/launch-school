def order_by_value(letters: dict):
    return sorted(letters, key=lambda x: letters[x])

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True