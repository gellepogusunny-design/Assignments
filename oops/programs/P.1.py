# classes_objects.py
class Car:
    """Class: blueprint for cars."""
    def __init__(self, make, model, year):
        self.make = make        # attribute
        self.model = model
        self.year = year

    def description(self):     # method
        return f"{self.year} {self.make} {self.model}"

# create (instantiate) objects
car1 = Car("Honda", "Civic", 2020)
car2 = Car("Toyota", "Corolla", 2022)

print(car1.description())  # 2020 Honda Civic
print(car2.description())  # 2022 Toyota Corolla
