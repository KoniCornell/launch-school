cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for city in cities:
    if city == None:
        continue
    print(f'The city {city} has {len(city)} letters.')




