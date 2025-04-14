class Vehicle:

    def __init__(self, wheels):
        self._wheels = wheels
        print(f'I have {self._wheels} wheels.')

    def drive(self):
        print('I am driving.')

class Car(Vehicle):

    def __init__(self):
        print('Creating a car.')
        super().__init__(4)

class Truck(Vehicle):

    def __init__(self):
        print('Creating a truck.')
        super().__init__(18)

class Motorcycle(Vehicle):

    def __init__(self):
        print('Creating a motorcycle.')
        super().__init__(2)

    def drive(self):
        super().drive()
        print('No! I am riding!')

car = Car()         # A car has been created.
                    # I have 4 wheels
car.drive()         # I am driving.
print()

truck = Truck()     # A truck has been created.
                    # I have 18 wheels
truck.drive()       # I am driving.
print()

motorcycle = Motorcycle()
# A motorcycle has been created.
# I have 2 wheels

motorcycle.drive()  # I am driving.
                    # No! I am riding!