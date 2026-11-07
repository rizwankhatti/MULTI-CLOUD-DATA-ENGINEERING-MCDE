# Task 07 - Payroll Engine
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_pay(self):
        pass

class Salaried(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary
    def calculate_pay(self):
        return self.salary

class Hourly(Employee):
    def __init__(self, name, rate, hours):
        super().__init__(name)
        self.rate = rate
        self.hours = hours
    def calculate_pay(self):
        overtime = max(0, self.hours - 40)
        return (self.hours - overtime) * self.rate + overtime * self.rate * 1.5

class Commission(Employee):
    def __init__(self, name, base, sales, rate):
        super().__init__(name)
        self.base = base
        self.sales = sales
        self.rate = rate
    def calculate_pay(self):
        return self.base + self.sales * self.rate

for e in [Salaried("Ahmed", 50000), Hourly("Sana", 20, 45), Commission("Usman", 500, 4000, 0.10)]:
    print(e.name, e.calculate_pay())
