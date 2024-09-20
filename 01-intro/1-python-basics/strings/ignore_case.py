name_1 = 'Roger'
name_2 = 'DAVE'

print(name_1.lower() == 'RoGeR'.lower())
print(name_2.lower() == 'DavE'.lower())
print(name_1.lower() == name_2.lower())

# another way using .casefold()
'''
The str.casefold method offers a more comprehensive approach to 
normalizing case than str.lower. It's primarily designed to 
facilitate case-insensitive string comparisons, especially in 
languages where conventional methods of converting to lowercase may fall short.
'''

name = 'Roger'
print(name.casefold() == 'RoGeR'.casefold())      # True
print(name.casefold() == 'DAVE'.casefold())       # False