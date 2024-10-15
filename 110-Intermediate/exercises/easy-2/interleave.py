def interleave(lst1: list, lst2: list):
    return [item for items in zip(lst1, lst2) for item in items]

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)