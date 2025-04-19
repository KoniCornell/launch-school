class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, width):
        super().__init__(width, width)

rect = Rectangle(4, 5)

print(rect.width == 4)        # True
print(rect.height == 5)       # True
print(rect.area == 20)        # True

print()
square = Square(5)
print(square.area == 25)      # True