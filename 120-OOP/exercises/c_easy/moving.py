class WalkMixin:
    def walk(self):
        return f"{self} {self.gait()} forward"

class Person(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

    def __str__(self):
        return self.name

class Cat(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

    def __str__(self):
        return self.name

class Cheetah(WalkMixin):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"

    def __str__(self):
        return self.name

class Noble(WalkMixin):
    def __init__(self, name, title):
        self.name = name
        self.title = title

    def __str__(self):
        return f"{self.title} {self.name}"

    def gait(self):
        return "struts" 
mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"

byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"

print(type(byron).__name__)
print(byron.__class__)