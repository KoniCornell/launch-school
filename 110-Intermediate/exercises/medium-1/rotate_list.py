'''
PEDAC:
    1. Understand the Problem
        - Input: empty list, type(input) != list, list
        - Output: empty list, None, list
        Rules:
        Explicit: 
            - Rotate a list by:
                1. Move the 1st element to the end
                2. Do not modify the original list
            - If the input is an empty list, return an empty list.
            - If the input is not a list, return None.

        Implicit:
            -
        Questions:
            - 
    2. Examples
         - Provided in question
    3. Data Structures
         - 
    4. Algorithms
        i. Check if list is empty: return []
        2. Check parameter type != list: return None
        3. Create a copy list using [:]
        4. Pop first item and append to the end.
        5. Return the new list.
'''
import copy
def rotate_list(list_item: list):
    if list_item == []:
        return list_item
    elif type(list_item) != list:
        return None
    new_list_item = copy.deepcopy(list_item)
    first_item = new_list_item.pop(0)

    new_list_item.append(first_item)
    # print(new_list_item)

    return new_list_item


# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])


