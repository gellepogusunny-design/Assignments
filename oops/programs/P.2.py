# attributes_methods.py
class Circle:
    pi = 3.14159           # class attribute

    def __init__(self, radius):
        self.radius = radius  # instance attribute

    def area(self):            # instance method
        return Circle.pi * self.radius * self.radius

    @classmethod
    def unit_circle(cls):     # class method
        return cls(1)

    @staticmethod
    def info():               # static method
        return "Area = pi * r^2"

c = Circle(3)
print(c.area())             # 28.27431
u = Circle.unit_circle()
print(u.radius)             # 1
print(Circle.info())        # Area = pi * r^2
