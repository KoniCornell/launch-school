print()

car = {
    'type' : 'sedan',
    'color' : 'blue',
    'mileage' : 80000,

}

car['year'] = 2003

# del car['mileage'] #(remove the key and its value)

print(car)

print(car['color']) # select and print the value 'blue' from the car object



# Check whether the keys 'name' and 'type' exist in car
print('name' in car)      # False
print('type' in car)     # True