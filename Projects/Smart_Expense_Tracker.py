#This is a program to help with financial management

print("Welcome to your personal Smart Expense Tracker")
Day_job = int(input("Salary K"))
Side_hustle = int(input("Side Hustle K"))
Freelancing = int(input("Freelancing K"))
#Total Net Income
Total_Net_Income = Day_job + Side_hustle + Freelancing
print(f'\tYour Total Net Income is: {Total_Net_Income}')

#Expenses section
print("\nPlease enter all expenses applicable to you")
#Fundamental expenses
fundamentals = {
    "rent": int(input("Rent: ")),
    "food": int(input("Food: ")),
    "electricity": int(input("Electricity:")),
    "water": int(input("Water: ")),
   }

#Recreation and fun expenses
print("Please enter all expenses about fun and recreation")
fun = {
    "clothing": int(input("Clothing: ")),
    "eating out": int(input("Eating out K")),
    "movies": int(input("Movie K")),
    "facials": int(input("Facials K")),
}
#Savings for future use
print("Please enter all your savings for the future")
savings = {
    "emergency": int(input("Emergency K")),
    "self-development": int(input("Self-Development K")),
    "education": int(input("Education K")),
    }
# # Calling a function
# indicators.categories(fundamentals)
# indicators.categories(fun)
# indicators.categories(savings)

#showing details of the fundamentals
print("Here is a summary of your fundamentals:")
for key, value in fundamentals.items():
    print(f'\t{key.title()}: {value}')
total_fundamentals = sum(fundamentals.values())

#showing details of the recreation and fun
print("Here is a summary of your recreation budget:")
for key, value in fun.items():
    print(f'\t{key.title()}: {value}')
total_recreation = sum(fun.values())

#showing details of the savings
print("Here is a summary of all your savings")
for key, value in savings.items():
    print(f'\t{key.title()}: {value}')
total_savings = sum(savings.values())

#Total expenses
print("Here is the total of all your expenses")
print(f'\tFundamentals: {total_fundamentals}')
print(f'\tRecreation: {total_recreation}')
print(f'\tSavings: {total_savings}')

#Grand total of all expenses
grand_total = total_fundamentals + total_recreation + total_savings
print(f"Total Expenses: {grand_total}")
#Condition
if grand_total > Total_Net_Income:
    deficit = grand_total - Total_Net_Income
    print("You are spending more that you earn")
    print(f'You spend K{deficit}, this means you owe someone or you have an overdraft.')
else:
    surplus = Total_Net_Income - grand_total
    print(f'You have K{surplus}, remaining from your income, please save it for future use.')

#Indicator of goals
"""Fundamentals Indicators"""
def essentials():
    goal = 60
    actual = ((total_fundamentals/Total_Net_Income) * 100)
    total = total_fundamentals
    if actual > goal:
        print("\tYou are using more on your needs. Please consider reviewing your lifestyle")
    elif goal > actual:
        essentials2save = int((goal - actual) * (total / 100))
        print(f'\tYou have K{essentials2save} remaining '
              f'from your fundamentals budget, please push it to savings.')

"""Recreation Indicators"""
def recreation():
    goal = 30
    actual = ((total_recreation/Total_Net_Income) * 100)
    total = total_recreation
    if actual > goal:
        print("\tYou are using more money for fun. Please consider reviewing your lifestyle.")
    elif goal > actual:
        recreation2save = int((goal - actual) * (total / 100))
        print(f'\tYou have K{recreation2save} remaining '
              f'from your recreation budget, please push it to savings.')

"""Savings Indicators"""
def savings():
    goal = 20
    actual = ((total_savings/Total_Net_Income) * 100)
    total = total_savings
    if actual > goal:
        print("\tYou are on a good note because you are saving more than anticipated.")
    elif goal > actual:
        print(f'\tPlease aim to save K{int((goal - actual) * (total / 100))} more to be safe.')
#Calling the functions
essentials()
recreation()
savings()