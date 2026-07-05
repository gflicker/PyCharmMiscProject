class Fundamentals:
    """Class to represent the fundamentals class"""
    def __init__(self, name, amount):
        """Initializing the fundamentals class"""
        self.name = name
        self.amount = amount
        self.expenses = {}

    def get_expenses(self):
        """Getting the description and amount of each expense and add them to a dictionary"""
        enter = True
        while enter:
            self.name = input("Enter name of the expense (q to quit): ")
            self.name = self.name.lower()
            if self.name == 'q':
                enter = False
            else:
                self.amount = int(input("Enter amount (q to quit): "))
                self.expenses[self.name] = self.amount


    def expenses_summary(self):
        """Printing out all expenses that have been added to the expenses dictionary"""
        print('\t=================================')
        for key, value in self.expenses.items():
            key = key.title()
            print(f"\t{key}                K{value}")

    def total_expenses(self):
        """Adding up each value in the dictionary of expenses to get the total"""
        total = sum(self.expenses.values())
        print(f'\t__________________________________')
        print(f'\tTotal                        K{total}')
