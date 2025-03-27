def multiply_items(lst1: int, lst2: int):
    return [i * j for i, j in zip(lst1, lst2)]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True