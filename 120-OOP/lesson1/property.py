class GoodDog:

    def __init__(self, name, age):
        self.name = name # calls name.setter
        self.age = age  # calls age.setter

    # Why self.name and not self._name? same with self.age? Think!(answer below)

    def speak(self):
        return f'{self.name} says arf!'
    
    # @property turns a method into something that acts like an attribute.
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('Name must be a string')

        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise TypeError('Age must be an integer')

        if age < 0:
            raise ValueError("Age can't be negative")

        self._age = age

sparky = GoodDog('Sparky', 5)
print(sparky.name)          # Sparky
print(sparky.age)           # 5
sparky.name = 'Fireplug'

print(sparky.name)          # Fireplug
sparky.age = 6
print(sparky.age)           # 6

sparky.name = 42  # TypeError: Name must be a string

sparky.age = -1   # ValueError: Age can't be negative


print(GoodDog.mro())

'''
Why go through the setter?

Using self.name = name:

1. Triggers the @name.setter, which may include:
    - Validation (e.g., making sure the name isn't empty).
    - Logging.
    - Transformation (e.g., capitalizing the name).

2. Keeps behavior consistent across the class, so all changes to name go through 
    the same logic.

Using self._name = name:
    - Bypasses the setter completely.
    - Might be used in rare cases where you're sure you don’t need validation 
        (e.g., during internal setup).
'''