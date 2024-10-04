# # Question 2 What does the last line in the following code output?
# dictionary = {'first': [1]}
# num_list = dictionary['first']
# num_list.append(2)

# print(num_list)     # [1, 2]
# print(dictionary)   # {'first': [1, 2]}

MONTHS = {
    1: 'JaNuArY',
    2: 'february',
    3: 'MaRch',
    4: 'ApriL',
    5: 'mAY',
    6: 'jUne',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'oCTOber',
    11: 'november',
    12: 'deCember'
}

month_names = MONTHS.values()
print(type(month_names))

def cap_values(d):
    for key, value in d.items():
        d[key] = value.capitalize()

    return d

capitalized_months = cap_values(MONTHS)
print(capitalized_months is MONTHS)
print(list(month_names))
# ['January', 'February', 'March', 'April',
#   'May', 'June', 'July', 'August', 'September',
#   'October', 'November', 'December']


for i in range(5):
    print(i)

capitalized_months[1] = 'December'

print(MONTHS)