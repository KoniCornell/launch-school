'''
Pedac:
1. Understanding the problem
    - Input: List of numbers
    - Output: List of numbers
    - Rules:
        a. Explicit:
            - Parameter is a list of numbers
            - Compare each number to the other numbers
            - Find how many numbers are smaller than it
            - Count only unique values
            - Return each count as a list
        b. Implicit:
            - The numbers are of type int
            - List is not empty
    - Questions:
        - 
2. Examples:
    print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
    print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
    print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
    print(smaller_numbers_than_current([1]) == [0])

    my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
    result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
    print(smaller_numbers_than_current(my_list) == result)

3. Data Structures:
    - List
    - Set
4. Algorithm:
    - Create a set of the list of numbers to remove duplicates
    - Loop through the list of numbers
    - Create a list of the smaller values in the set
    - Count the numbers
    - return a list

5. Code with intent

'''

def smaller_numbers_than_current(list_of_numbers: list):
    set_of_numbers = set(list_of_numbers)
    numbers_count = []

    for i in list_of_numbers:
        new_list = []

        for j in set_of_numbers:
            if j < i:
                new_list.append(j)
        numbers_count.append(len(new_list))

    return numbers_count


print(smaller_numbers_than_current([8, 1, 2, 2, 3]) == [3, 0, 1, 1, 2])
print(smaller_numbers_than_current([7, 7, 7, 7]) == [0, 0, 0, 0])
print(smaller_numbers_than_current([6, 5, 4, 8]) == [2, 1, 0, 3])
print(smaller_numbers_than_current([1]) == [0])

my_list = [1, 4, 6, 8, 13, 2, 4, 5, 4]
result   = [0, 2, 4, 5, 6, 1, 2, 3, 2]
print(smaller_numbers_than_current(my_list) == result)