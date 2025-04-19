'''
Instance variables can be set to any object, even an object of a custom class
     you've created.
'''
class Person:
    def __init__(self):
        self._heroes = ['Superman', 'Spiderman', 'Batman']
        self.cash = {
            1:   12,  # The key is bill value, value is count
            2:   1,
            5:   2,
            10:  3,
            20:  2,
            50:  1,
            100: 1,
        }

    def cash_on_hand(self):
        return sum([bill_value * count
                    for (bill_value, count) in self.cash.items()])

    def heroes(self):
        return ', '.join(self._heroes)

joe = Person()
print(joe.cash_on_hand())  # 244
print(joe.heroes())        # Superman, Spiderman, Batman

''' Example II '''
class Person:
    def __init__(self, name):
        self.name = name

class Dog:
    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'

class Bulldog(Dog):
    pass

bob = Person('Robert')
bud = Bulldog()

bob.pet = bud
print(bob.pet)      # <__main__.Bulldog object at 0x105001f50>

# We've created a brand new self.pet instance variable in bob, and assigned it
# to the Bulldog object, bud. Thus, when we reference bob.pet on the last line, 
# it returns a Bulldog object.
 
# Since bob.pet returns a Bulldog object, we can chain any Bulldog methods 
# to the return value:

print(bob.pet.speak())        # bark!
print(bob.pet.fetch())        # fetching!