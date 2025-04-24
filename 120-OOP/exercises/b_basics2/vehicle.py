class Vehicle:
    def __init__(self, year):
        self._year = year

    @property
    def year(self):
        return self._year
    
    def start_engine(self):
        return 'Ready to go!'

class Truck(Vehicle):
    def __init__(self, year, bed_type):
        super().__init__(year)
        self._bed_type = bed_type

    def start_engine(self, speed):
        return f'{super().start_engine()} Drive {speed}, please!'  
    
    @property
    def bed_type(self):
        return self._bed_type

class Car(Vehicle):
    pass

# Comments show expected output
truck1 = Truck(1994, 'Short')
print(truck1.year)            # 1994
print(truck1.bed_type)        # Short
print(truck1.start_engine('fast'))
print()
print(truck1.start_engine('slow'))

print()
car1 = Car(2006)
print(car1.year)              # 2006
# print(car1.bed_type)
# AttributeError: 'Car' object has no attribute 'bed_type'