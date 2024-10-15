
def union(lst1: list, lst2: list):
    return set(lst1 + lst2)


print(union([1, 3, 5], [3, 6, 9]) == {1, 3, 5, 6, 9}) # True