# inheritance_examples.py

# 1) Single inheritance
class Animal:
    def speak(self):
        return "some sound"

class Dog(Animal):   # single
    def speak(self):
        return "woof"

# 2) Multiple inheritance
class Flyer:
    def fly(self):
        return "flying"

class Swimmer:
    def swim(self):
        return "swimming"

class Duck(Flyer, Swimmer):  # multiple
    pass

# 3) Multilevel inheritance (A -> B -> C)
class LivingThing:
    pass

class Plant(LivingThing):
    pass

class Flower(Plant):
    def name(self):
        return "rose"

# 4) Hierarchical inheritance (one parent, many children)
class Shape:
    def area(self):
        raise NotImplementedError

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side * self.side

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14 * self.r * self.r

# 5) Hybrid inheritance (combination example)
class A:
    def a(self): return "A"

class B(A):
    def b(self): return "B"

class C(A):
    def c(self): return "C"

class D(B, C):  # D inherits from B and C which both inherit A -> hybrid
    pass
