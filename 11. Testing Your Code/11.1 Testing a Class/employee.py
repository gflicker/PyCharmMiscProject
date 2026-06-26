# A class which has the attributes of the employee and salary
class Employee:
    """Employee's name and salary"""
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.annual_salary = 5000

    """A method for the default raise salary of an employee"""
    def give_default(self):
        description = f'{self.first} {self.last} {self.annual_salary}'
        return description

    """A method for the custom raise salary of an employee"""
    def give_raise(self, amount = 5000):
        self.annual_salary += amount
        increased = f'{self.first} {self.last} {self.annual_salary}'
        return increased


