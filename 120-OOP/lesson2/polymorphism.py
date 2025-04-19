class Animal:
    def move(self):
        print(f'I am a {self.__class__.__name__}: I am not moving.')
    
class Fish(Animal):
    def move(self):
        print(f'I am a {self.__class__.__name__}: I am swimming.')

class Cat(Animal):
    def move(self):
        print(f'I am a {self.__class__.__name__}: I am walking.')

class Sponge(Animal):
    pass

class Coral(Animal):
    pass

animals = [Fish(), Cat(), Sponge(), Coral()]

for animal in animals:
    animal.move()