class SwimMixin:
    def swim(self):
        return 'Swimming!'
    
class Pet:
    def speak(self):
        pass

class Mammal(Pet):
    def run(self):
        return 'Running!'
    
    def jump(self):
        return 'Jumping!'
    
class Dog(SwimMixin, Pet):
    def speak(self):
        return 'Bark!'
    
    def fetch(self):
        return 'Fetching!'

class Bulldog(Dog):
    def swim(self):
        return "Can't Swim!"

class Fish(SwimMixin, Pet):
    pass

class Cat(Mammal):
    def speak(self):
        return 'Meow'
    
print(Fish.mro())
print()
print(Bulldog.mro())