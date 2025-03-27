'''
Pedac:
1. Understanding the problem
    - Input: List of integers
    - Output: Int or in a special case: None
    - Rules:
        a. Explicit: 
            - Given a list of integers
            - Calculate minimum sum of 5 consecutive numbers
                in the list
            - Return the value
            - If len(list of int) < 5: return None
        b. Implicit:
            - The list is not empty.
    - Questions:
        - 
2. Examples
    print(minimum_sum([1, 2, 3, 4]) is None)
    print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
    print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
    print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
    print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)

3. Data Structures:
    - List

4. Algorithm:
    - Get len(list of integers)
    - return None if it is less than 5
    - Create an empty list for sums
    - Find sum for each 5 elements in the list
    - Add the sum to the empty list
    - Stop when the last index is == len(list) + 1
    - Get min(empty list) and return it

5. Code with intent
'''

def minimum_sum(list_of_int: list):
    length = len(list_of_int)

    if length < 5:
        return None
    
    start = range(length)
    stop = range(5, length + 1)

    idx = zip(start, stop)

    sums = []

    for i, j in idx:
        sums.append(sum(list_of_int[i:j]))

    # print(sums)
    # print(min(sums))

    return min(sums)


print(minimum_sum([1, 2, 3, 4]) is None)
print(minimum_sum([1, 2, 3, 4, 5, -5]) == 9)
print(minimum_sum([1, 2, 3, 4, 5, 6]) == 15)
print(minimum_sum([55, 2, 6, 5, 1, 2, 9, 3, 5, 100]) == 16)
print(minimum_sum([-1, -5, -3, 0, -1, 2, -4]) == -10)