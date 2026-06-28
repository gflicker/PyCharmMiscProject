#Creating a budget tracker incorporating classes in it
class Income:
    def __init__(self, day_job, side_hustle, freelancing):
        self.day_job = day_job
        self.side_hustle = side_hustle
        self.freelancing = freelancing
        #Prompting for the figures from each income stream
    def income_sources(self):
        #Total income
        print("Income Sources")
        total_income = self.day_job + self.side_hustle + self.freelancing
        print(f'Here is a summary of your your income')
        print(f'\tDay Job: {self.day_job} \n\tSide Hustle: {self.side_hustle} '
              f'\n\tFreelancing: {self.freelancing}' )

        print("Total Income: K",total_income)

"""A method that will help with computing the Fundamental expenses"""
class Fundamentals:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    #A method for the fundamentals
    def fundamental_needs(self):
        print("Fundamental Expenses")
        filename = 'fundamentals.txt'
        active = True
        while active:
            self.category = input("Category: ")
            self.amount = input("Amount: ")

            if self.category == "q":
                active = False
                with open(filename) as expenses:
                    needs = expenses.read()
                print(needs)
                print("Enter all expenses that are for recreation")

            else:
                with open(filename, 'a') as expenses:
                    expenses.write(f"{self.category}: {self.amount}\n")
                    print("Enter another category (q to quit)")

class Fun(Fundamentals):
    def __init__(self, category, amount):
        super().__init__(category, amount)

"""An instance for calculating my total income"""
my_income = Income(int(input("Day Job: ")), int(input("Side Hustle: ")),
                   int(input("Freelancing: ")))
my_income.income_sources()

"""An instance for calculating my total expenses for home essentials"""
essential_needs = Fundamentals(category='', amount=0)
essential_needs.fundamental_needs()

"""An instance for calculating my total expenses for recreation"""
my_fun = Fun(category='', amount=0)
my_fun.fundamental_needs()

