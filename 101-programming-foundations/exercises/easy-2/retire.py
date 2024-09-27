from datetime import datetime as dt

year = dt.now().year

age_now = int(input('What is your age: '))
age_retire = int(input('At what age would you like to retire? '))

difference = age_retire - age_now

print(f"It's {year}. You will retire in {year + difference}.")
print(f'You have only {difference} years of  work to go!')