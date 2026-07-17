#My personal Expenses Tracker and Report

from fundamentals import*

class Income:
    """Defining a function that will initialize income streams"""
    def __init__(self, day_job, side_hustle, freelancing):
        self.day_job = day_job
        self.side_hustle = side_hustle
        self.freelancing = freelancing
        self.other_sources = {}
        self.extras = float(0)

    def get_income(self):
        """A function for calculating the total income"""
        self.day_job = self.get_valid_amount('Day Job Amount: ')
        self.side_hustle = self.get_valid_amount('Side Hustle Amount: ')
        self.freelancing = self.get_valid_amount('Freelancing Amount: ')

    def get_extra_income(self):
        """A function for calculating the extra income"""
        start = True
        while start:
            decision = input("Do you have other sources of income? (yes/no): ")
            decision = decision.lower()
            if decision == 'no':
                start = False
                break
            else:
                other = input("Enter the source of income: ")
                amount = self.get_valid_amount(f'{other} Amount: ')
                self.other_sources[other] = amount # or other_sources.update({other:amount})
                self.extras += amount

    def get_valid_amount(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Please enter a numeric value")

    def calculate_total_income(self):
        """A function for calculating the total income"""
        total_income = self.day_job + self.side_hustle + self.freelancing + self.extras
        return total_income

    def income_summary(self):
        """A function for printing the income summary"""
        #Making variables to properly format the padding and spacing
        day_job = "Day Job:"
        side_hustle = "Side Hustle:"
        freelancing = "Freelancing:"
        total_income = "Total Income:"
        summary_banner = "\n===============INCOME SUMMARY================"
        lower_line = "--------------------------------------------"

        print(f'{summary_banner:^50}')
        print(f'{day_job:<35} K{self.day_job}')
        print(f'{side_hustle:<35} K{self.side_hustle}')
        print(f'{freelancing:<35} K{self.freelancing}')

        """Printing the other sources of income"""
        for source, value in self.other_sources.items():
            source = source.title()
            print(f'{source:<35} K{value}')
        print(f'{lower_line:<35}')
        print(f'{total_income:<35} K{self.calculate_total_income()}')
        return

    def save_income_data(self):
        filename = "Projects/modules/income.txt"
        with open(filename, "w") as income_file:
            json.dump(self.other_sources, income_file)


#Creating and calling an instance of the object
my_income = Income(day_job=0, side_hustle=0, freelancing=0)
print("=======PERSONAL EXPENDITURE TRACKER========")
print("My Income Sources")

my_income.get_income()
my_income.get_extra_income()

"""Calling all instances to do with fundamental expenses"""
my_needs = Fundamentals()
my_needs.get_fundamental_category()
my_needs.get_expenses()

my_fun = Fun()
my_fun.get_fun_category()
my_fun.get_expenses()

my_savings = Savings()
my_savings.get_saving_category()
my_savings.get_expenses()

my_income.income_summary()
my_needs.get_fundamental_category()
my_needs.expenses_summary()
my_needs.total_expenses()

my_fun.get_fun_category()
my_fun.expenses_summary()
my_fun.total_expenses()

my_savings.get_saving_category()
my_savings.expenses_summary()
my_savings.total_expenses()

"""Saving data to a text file"""
my_needs.save_data()
my_fun.save_data()
my_savings.save_data()

"""Determining Total Expenses for all three categories, to control overspending"""
available_cash = my_income.calculate_total_income()
fundamental_subtotal = my_needs.total_expenses()
fun_subtotal = my_fun.total_expenses()
savings_subtotal = my_savings.total_expenses()
grand_expenses = fundamental_subtotal + fun_subtotal + savings_subtotal
remainder = available_cash - grand_expenses

#These are for formatting purposes only.
grand_padding = "Total Expenses:"
payout_padding = "Payout Balance:"
sub_summary = "\n=============SUBTOTAL SUMMARY============="
subtotal_line = "------------------------------------------"
available_padding = "Available Cash"
fundamental_banner = "Fundamental Expenses"
recreation_banner = "Fun Expenses"
savings_banner = "Savings"

print(f'{sub_summary:^35}')
print(f'{payout_padding:<35}: K{available_cash}')
print(f'{fundamental_banner:<35}: K{fundamental_subtotal}')
print(f'{recreation_banner:<35}: K{fun_subtotal}')
print(f'{savings_banner:<35}: K{savings_subtotal}')

print(f'{subtotal_line:^35}')
print(f'{grand_padding:<35} K{grand_expenses}')
print(f'{subtotal_line:^35}')
print(f'{available_padding:<35} K{remainder}')

"""This is a report section, indicating how much of each category has been used."""
report = "============REPORT SUMMARY============"
print(f'\n{report:^35}')

fundamental_quota = ((50/100) * available_cash)
fun_quota = ((30/100) * available_cash)
savings_quota = ((20/100) * available_cash)

if remainder < 0:
    print("Sorry you spent more than you earn.")
    print(f'Kindly cut the following from your budget:')
    if fundamental_subtotal > fundamental_quota:
        print(f"{fundamental_banner}: K{fundamental_subtotal - fundamental_quota}")

    if fun_subtotal > fun_quota:
        print(f'{recreation_banner}: K{fun_subtotal - fun_quota}')

    if savings_subtotal > savings_quota:
        print(f'{savings_banner}: K{savings_subtotal - savings_quota}')

"""Fundamental Expenses report"""
print(f'\n{fundamental_banner}')
if fundamental_subtotal > fundamental_quota:
    print(f"You spent K{fundamental_subtotal - fundamental_quota} more "
          f"than allocated amount.")
elif fundamental_subtotal == fundamental_quota:
    print("You spend exactly the allocated amount. Keep spending smart")
else:
    print(f'You have spent less than allocated, consider spending'
          f'K{fundamental_quota - fundamental_subtotal} more.')

"""Fun Expenses Report"""
print(f'\n{recreation_banner}')
if fun_subtotal > fun_quota:
    print(f"You have spent K{fun_subtotal - fun_quota} more "
          f"than allocated amount.")
elif fun_subtotal == fun_quota:
    print("You spent exactly the allocated amount, keep spending smart")
else:
    print(f'You have spent less than allocated, consider spending'
          f' K{fun_quota - fun_subtotal} more.')

"""Savings Report"""
print(f'\n{savings_banner}')
if savings_subtotal > savings_quota:
    print(f"You have spent K{savings_subtotal - savings_quota} more "
          f"than allocated amount.")
elif savings_quota == savings_subtotal:
    print("You saved exactly the allocated amount. Keep saving smart")
else:
    print(f'You saved less than allocated, consider saving'
          f' K{savings_quota - savings_subtotal} more.')

print("\nSpend wisely and don't forget to save for a rainy day.")