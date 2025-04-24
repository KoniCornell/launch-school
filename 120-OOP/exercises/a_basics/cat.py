class Cat:

    counter = 0

    def __init__(self, name):
        self._name = name
        type(self).counter += 1
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
    
    def __str__(self):
        return f"I'm {self.name}!"
    
    def greet(self):
        print(f'Hello! My name is {self.name}!')

    @classmethod
    def generic_greeting(cls):
        print(f"Hello! I'm a {cls.__name__}!")

    def identify(self):
        return self

    def rename(self, new_name):
        self.name = new_name

    @classmethod
    def total(cls):
        print(cls.counter)

# Empty class
# When naming a class, the PascalCase format is used instead of the 
# snake_case format.


kitty = Cat('Sophie')
print()
Cat.generic_greeting()
print()

kitty.greet()
print(kitty.name)
print()

kitty.name = 'Luna'
kitty.greet()
print(kitty.name)

print()
kitty.rename('Chloe')
print(kitty.name)             # Chloe

print()
print(kitty.identify())

print()
Cat.total()         # 0

kitty1 = Cat("lala")
Cat.total()         # 1

kitty2 = Cat('Po')
Cat.total()         # 2

print(Cat)        # <__main__.Cat object at 0x104ed7290>
Cat.total()         # 3