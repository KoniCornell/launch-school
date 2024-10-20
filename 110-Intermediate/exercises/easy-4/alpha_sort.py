def alphabetic_number_sort(numbers: list):
    # numbers.sort(key= lambda x: numbers_dict[x])
    # using list.sort mutates the list and return Nine
    return sorted(numbers, key = lambda x: numbers_dict[x])


'''
instead of using lambda
create a function and use it as a key.
'''


# def numbers_values(num: int):
#     return numbers_dict[num]

# def alphabetic_number_sort(numbers: list):
#     numbers.sort(key= numbers_values)
#     return numbers

number_names = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 
                'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 
                'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 
                'eighteen', 'nineteen']

numbers_dict = {idx: name for idx, name in enumerate(number_names)}

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result)
# Prints True
print(alphabetic_number_sort(input_list))