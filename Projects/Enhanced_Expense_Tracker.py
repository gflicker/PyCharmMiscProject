#This is a program to help with financial management
from modules import indicators

print("Welcome to your personal Smart Expense Tracker")
day_job = int(input("Salary: K"))
side_hustle = int(input("Side Hustle: K"))
freelancing = int(input("Freelancing: K"))

#Total Net Income
total_net_income = day_job + side_hustle + freelancing
print(f'\tYour Total Net Income is: K{total_net_income}')

#Expenses section
print("\nPlease enter all expenses applicable to you")
#Fundamental expenses
fundamentals = {
    "rent": int(input("Rent: K")),
    "food": int(input("Food: K")),
   }

#Recreation and fun expenses
print("\nPlease enter all expenses about fun and recreation")
recreation = {
    "clothing": int(input("Clothing: K")),
    "eating out": int(input("Eating out :K")),
    }
#Savings for future use
print("\nPlease enter all your savings for the future")
savings = {
    "emergency": int(input("Emergency: K")),
    "self-development": int(input("Self-Development: K")),
    }
#Calling a function
"""The summary of all expenses for each category of expenses"""
indicators.categories(fundamentals)
indicators.categories(recreation)
indicators.categories(savings)

"""Total of all expenses, adding each category's total expenses"""
total_sum = sum(fundamentals.values()) + sum(recreation.values()) + sum(savings.values())
print(f'Here is the total of all expenses: K{total_sum}.')
"""What is remaining from the income after deductions"""
remainder = total_net_income - total_sum
print(f'\n You are remaining with K{remainder}.')
"""Indicators to monitor spending in line with financial goals"""
def essentials():
    goal = 60
    actual = (sum(fundamentals.values()) / total_net_income) * 100
    essentials_percentage = int((goal - actual) * 100)

    if actual > goal:
        print("\tYou are using more on your needs. Please consider reviewing your lifestyle")
    elif goal > actual:
        essentials2save = int((goal - actual) * (essentials_percentage / 100))
        print(f'\tYou have K{essentials2save} remaining '
              f'from your fundamentals budget, please push it to savings.')

"""Recreation Indicators"""
def recreations():
    goal = 30
    actual = (sum(recreation.values()) / total_net_income) * 100
    recreation_percentage = int((goal - actual) * 100)

    if actual > goal:
        print("\tYou are using more money for fun. Please consider reviewing your lifestyle.")
    elif goal > actual:
        recreation2save = int((goal - actual) * (recreation_percentage / 100))
        print(f'\tYou have K{recreation2save} remaining '
              f'from your recreation budget, please push it to savings.')

"""Savings Indicators"""
def saving():
    goal = 20
    actual = (sum(savings.values()) / total_net_income) * 100
    savings_percentage = int((goal - actual) * 100)

    if actual > goal:
        print("\tYou are on a good note because you are saving more than anticipated.")
    elif goal > actual:
        print(f'\tPlease aim to save K{int((goal - actual) * (savings_percentage / 100))} more to be safe.')
#Calling the functions
essentials()
recreations()
saving()

"""Total savings of the month"""
from_fundamentals = int(input("\nEnter remainder from Fundamentals: K"))
from_recreation = int(input("Enter remainder from Recreation: K"))
total_amount_saved = remainder + from_fundamentals + from_recreation
print(f'Congrats, you have managed to save K{total_amount_saved}. Keep it safe.')

