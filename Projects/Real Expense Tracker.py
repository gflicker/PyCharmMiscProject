#My personal Expenses Tracker and Report
from fundamentals import Fundamentals

class Income:
    """Defining a function that will initialize income streams"""
    def __init__(self, day_job, side_hustle, freelancing):
        self.day_job = day_job
        self.side_hustle = side_hustle
        self.freelancing = freelancing
        self.extras = 0

    def get_income(self):
        """A function for calculating the total income"""
        self.day_job = float(input('Day Job Amount: '))
        self.side_hustle = float(input('Side Hustle Amount: '))
        self.freelancing = float(input('Freelancing Amount: '))

    def get_extra_income(self):
        """A function for calculating the extra income"""
        other_sources = {}
        start = True
        while start:
            decision = input("Do you have other sources of income? (yes/no): ")
            decision = decision.lower()
            if decision == 'no':
                start = False
                break
            else:
                other = input("Enter the source of income: ")
                amount = float(input(f'{other} Amount: '))
                other_sources[other] = amount # or other_sources.update({other:amount})
                self.extras += amount

    def calculate_total_income(self):
        """A function for calculating the total income"""
        total_income = self.day_job + self.side_hustle + self.freelancing + self.extras
        return total_income

    def income_summary(self):
        """A function for printing the income summary"""
        print("\n===========INCOME SUMMARY=============")
        print(f'Day Job:                      K{self.day_job}')
        print(f'Side Hustle:                  K{self.side_hustle}')
        print(f'Freelancing                   K{self.freelancing}')
        print(f'Extra Income:                 K{self.extras}')
        print("--------------------------------------")
        print(f'Total Income:                 K{self.calculate_total_income()}')

#Creating and calling an instance of the object
my_income = Income(day_job=0, side_hustle=0, freelancing=0)
my_income.get_income()
my_income.get_extra_income()
my_income.income_summary()

my_fundamental_expenses = Fundamentals("Fundamentals", amount=0)
my_fundamental_expenses.get_expenses()
my_fundamental_expenses.expenses_summary()
my_fundamental_expenses.total_expenses()
