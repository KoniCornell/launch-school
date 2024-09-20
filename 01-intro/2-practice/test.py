# forenames = ['Ken', 'Lynn', 'Pat', 'Nancy']
# surnames = ['Camp', 'Blake', 'Flanagan', 'Short']

# zipped_names = zip(forenames, surnames)

# #print(zipped_names)

# # for i in zipped_names:
# #     print(i)

# for forename, surname in zipped_names:
#     print(f'{forename} {surname}')

######

# dict comprehensions

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

my_dict = {name : len(name) for name in my_set}

print(my_dict)

# keys with odd lengths

my_dict_odd = {name : len(name)
               for name in my_set
               if len(name) % 2 != 0}

print(my_dict_odd)