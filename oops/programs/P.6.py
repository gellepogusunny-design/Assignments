# abstraction.py
from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def compute_pay(self):
        pass

class SalariedEmployee(Employee):
    def __init__(self, monthly_salary):
        self.monthly_salary = monthly_salary

    def compute_pay(self):
        return self.monthly_salary

class HourlyEmployee(Employee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    def compute_pay(self):
        return self.hours * self.rate

s = SalariedEmployee(3000)
h = HourlyEmployee(100, 20)
print(s.compute_pay(), h.compute_pay())  # 3000 2000
