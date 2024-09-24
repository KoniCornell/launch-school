

bill = float(input('What is the bill? '))
tip = float(input('What is the tip percentage? '))

tip = (tip / 100) * bill
total = bill + tip

print(f'The tip is ${tip:.2f}')
print(f'The total is ${total:.2f}')