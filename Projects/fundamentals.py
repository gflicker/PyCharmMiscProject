import json

class Fundamentals:
    """Class to represent the fundamentals class"""
    def __init__(self):
        """Initializing the fundamentals class"""
        self.expenses = {}
        
    def get_expenses(self):
        """Getting the description and amount of each expense and add them to a dictionary"""
        enter = True
        while enter:
            name = input("Enter name of the expense (q to quit): ")
            name = name.lower()
            if name == 'q':
                enter = False
            else:
                while True:
                    enter_amount = input("Enter amount (q to quit): ")
                    if enter_amount == "q":
                        enter = False
                        break
                    try:
                        amount = int(enter_amount)
                        self.expenses[name] = amount
                        break
                    except ValueError:
                        print('Please enter a numeric value')

    def expenses_summary(self):
        """Printing out all expenses that have been added to the expenses dictionary"""
        total_line = "_______________________________________"
        total_padding = "Sub Total:"
        for key, value in self.expenses.items():
            key = key.title()
            print(f"{key:<35} K{value}")
        total = self.total_expenses()
        print(f'{total_line:^40}')
        print(f"{total_padding:<35} K{total}")

    def total_expenses(self):
        """Adding up each value in the dictionary of expenses to get the total"""
        total = sum(self.expenses.values())
        return total

    def get_fundamental_category(self):
        fundamentals_banner = "Fundamental Expenses"
        print(f'\n{fundamentals_banner:^40}')
        return fundamentals_banner

    def data_filename(self):
        self.get_fundamental_category()
        filename = "fundamentals.txt"
        return filename

    def save_data(self):
        filename = self.data_filename()
        data_to_save = {
            "Expenses": self.expenses,
            "Total Expenses": self.total_expenses(),
        }
        with open(filename, 'w') as csvfile:
            json.dump(data_to_save, csvfile)


class Fun(Fundamentals):
    """Class to represent the fun or recreation expenses"""
    def get_fun_category(self):
        """Getting the expenses category of the fun"""
        recreation_banner = "Recreation Expenses"
        print(f'\n{recreation_banner:^40}')

    def data_filename(self):
        filename = "fun.txt"
        return filename


class Savings(Fundamentals):
    """Class to represent the savings expenses"""
    def get_saving_category(self):
        """Getting the savings name category and center align it"""
        savings_banner = "Savings"
        print(f'\n{savings_banner:^40}')

    def data_filename(self):
        filename = "savings.txt"
        return filename

