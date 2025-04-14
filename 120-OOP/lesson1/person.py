# PEDAC

'''
1. Understand the problem:
    Input:
    Output:
    Rules:
        Implicit:
        Explicit:
2. Examples
3. Data structures
4. Algorithms
5. Code with Intent

'''

class Person:
    def __init__(self, first_name, last_name):
        self.name = (first_name, last_name)


    @property
    def name(self):
        return f'{self._name[0].capitalize()} {self._name[1].capitalize()}'
    
    @name.setter
    def name(self, name):
        if not isinstance(name, tuple) or len(name) != 2:
            raise ValueError("Name must be a tuple of (first_name, last_name).")

        for word in name:
            if not word.isalpha():
                raise ValueError('Name must be a alphabetic.')
        
        self._name = name
    

actor = Person('Mark', 'Sinclair')
print(actor.name)              # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor.name)              # Vin Diesel
#actor.name = ('L0i', 'Diesel')
# ValueError: Name must be alphabetic.

character = Person('annIE', 'HAll')
print(character.name)          # Annie Hall
#character = Person('Da5id', 'Meier')
# ValueError: Name must be alphabetic.

friend = Person('Lynn', 'Blake')
print(friend.name)             # Lynn Blake
#friend.name = ('Lynn', 'Blake-John')
# ValueError: Name must be alphabetic.

'''
book code:
'''
# class Person:

#     def __init__(self, first_name, last_name):
#         self._set_name(first_name, last_name)

#     @property
#     def name(self):
#         first_name = self._first_name.title()
#         last_name = self._last_name.title()
#         return f'{first_name} {last_name}'

#     @name.setter
#     def name(self, name):
#         first_name, last_name = name
#         self._set_name(first_name, last_name)

#     @classmethod
#     def _validate(cls, name):
#         if not name.isalpha():
#             raise ValueError('Name must be alphabetic.')

#     def _set_name(self, first_name, last_name):
#         Person._validate(first_name)
#         Person._validate(last_name)
#         self._first_name = first_name
#         self._last_name = last_name