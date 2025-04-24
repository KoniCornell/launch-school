'''
Determine the method resolution order (MRO) used when accessing the 
cat1.color property
'''
class Animal:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

class Cat(Animal):
    pass

class Bird(Animal):
    pass

cat1 = Cat('Black')
print(cat1.color)

# C3 linearization (depth)
# Cat -> Animal



print(Cat.__mro__)
print(Cat.mro())
print()

print(cat1.__class__)
print(cat1.__class__.__mro__)
print(cat1.__class__.mro())
print()
print(type(cat1))
print(type(cat1).mro())
print(type(cat1).__mro__)