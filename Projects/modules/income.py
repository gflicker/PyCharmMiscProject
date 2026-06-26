#This is a program to help with financial management
def total_earnings():
    print("Welcome to your personal Smart Expense Tracker")
    Day_job = int(input("Salary K"))
    Side_hustle = int(input("Side Hustle K"))
    Freelancing = int(input("Freelancing K"))
    # Total Net Income
    Total_Net_Income = Day_job + Side_hustle + Freelancing
    print(f'\tYour Total Net Income is: {Total_Net_Income}')