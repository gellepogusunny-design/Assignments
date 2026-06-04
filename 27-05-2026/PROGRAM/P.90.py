class Shape:
    def __init__(self):
        pass  # Default constructor
    def area(self):
        return 0  # Shape's area is 0 by default

class Square(Shape):
    def __init__(self, length):
        super().__init__()  # Call the constructor of the parent class
        self.length = length
    def area(self):
        return self.length ** 2  # Calculate the area of the square

# Create instances of the classes
shape = Shape()
try:
    length_val = float(input("Enter the length of the square: "))
    square = Square(length_val)
    # Calculate and print the areas
    print("Shape's area by default:", shape.area())
    print("Area of the square:", square.area())
except ValueError:
    print("Invalid input. Please enter a numerical value for length.")
