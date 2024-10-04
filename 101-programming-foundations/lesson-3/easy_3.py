def is_color_valid(color):
    if color == "blue" or color == "green":
        return True
    else:
        return False
    
# uses two return statements unnecessarily

def is_color_valid(color):
    return color == "blue" or color == "green"

def is_color_valid(color):
    return color in ["blue", "green"]

everest = "Everest"
kilimanjaro = "Kilimanjaro"
fuji = "Fuji"

mountain_list = [everest, kilimanjaro, fuji]

for idx in range(len(mountain_list)):
    mountain_list[idx] += " " + str(len(mountain_list[idx]))

mountain_list  # ['Everest 7', 'Kilimanjaro 11', 'Fuji 4']

print(everest)


bar = 0
foo = []
baz = 3

try:
    qux = (bar or foo) and (baz / bar)
except ZeroDivisionError:
    qux = 0

if qux:
    print("Operation succeeded")
else:
    print("Operation failed")