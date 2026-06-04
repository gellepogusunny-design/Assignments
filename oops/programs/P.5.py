# polymorphism.py
class Animal:
    def sound(self):
        return "?"

class Cat(Animal):
    def sound(self):
        return "meow"

class Dog(Animal):
    def sound(self):
        return "woof"

# operator overloading
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __add__(self, other):  # overload +
        return Point(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(1, 2)
p2 = Point(3, 4)
print(p1 + p2)  # Point(4, 6)
