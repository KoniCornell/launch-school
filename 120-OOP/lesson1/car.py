class Car:
    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self.color = color
        self.speed = 0

    # model and year are read only while color can be changed.
    @property
    def model(self):
        return self._model 
    
    @property
    def year(self):
        return self._year 
    
    @property
    def color(self):
        return self._color 
    
    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError('Color must be a string.')
        
        self._color = color

    def engine_on(self):
        return f'Your {self.year} {self.color} {self.model} is turned on.'

    def accelerate(self, number):
        self.speed += number
        return f'You accelerated {number} mph.'

    def brake(self, number):
        self.speed -= number
        return f'You decelerated {number} mph.'

    def engine_off(self):
        self.speed = 0
        return f'Your {self.year} {self.color} {self.model} is turned off.'
    
    def car_speed(self):
        return f"Your car's speed is {self.speed} mph."
    
    def spray_paint(self, color):
        self.color = color
        return f'Your car is now painted {color}.'

    @staticmethod
    def gas(miles, fuel):
        return miles / fuel

    def mileage(self, miles, fuel):
        return f'{self.gas(miles,fuel)} miles per gallon'


lumina = Car('chevy lumina', 1997, 'white')

print(lumina.engine_on()) # The engine is on!
print(lumina.car_speed())    # Your speed is 0 mph.
print(lumina.accelerate(20))   # You accelerated 20 mph.
print(lumina.car_speed())    # Your speed is 20 mph.
print(lumina.accelerate(30))   # You accelerated 30 mph.
print(lumina.car_speed())    # Your speed is 50 mph.
print(lumina.brake(15))      # You decelerated 15 mph.
print(lumina.car_speed())    # Your speed is 35 mph.
print(lumina.brake(30))      # You decelerated 30 mph.
print(lumina.car_speed())    # Your speed is 5 mph.
print(lumina.engine_off())   # Let's park this baby!
                            # The engine is off
print(lumina.car_speed())    # Your speed is 0 mph.

print(lumina.spray_paint('Black'))

print(lumina.mileage(351, 13))


