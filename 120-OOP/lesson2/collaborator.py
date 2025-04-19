# In this code, a Car object is a collaborator of a Driver object since a 
# driver needs a car to drive. Likewise, an Engine object is a collaborator 
# of a Car object; a car needs an engine or it won't run.

class Engine:
    def start(self):
        pass

class Car:
    def __init__(self, engine):
        self.engine = engine

    def start(self):
        return self.engine.start()

class Driver:
    def __init__(self, car):
        self.car = car

    def drive(self):
        return self.car.start()

engine = Engine()
car = Car(engine)
driver = Driver(car)

class Person:
    def __init__(self, name):
        self.name = name

class Pet:
    def jump(self):
        return 'How high?'

class Dog(Pet):

    def speak(self):
        return 'bark!'

    def fetch(self):
        return 'fetching!'

class Bulldog(Dog):
    pass

class Cat(Pet):
    pass

bob = Person('Robert')
kitty = Cat()
bud = Bulldog()
bob.pets = [kitty, bud]
print(bob.pets)
# [<__main__.Cat object at 0x102daa410>,
#  <__main__.Bulldog object at 0x102daa450>]

for pet in bob.pets:
    print(pet.jump())