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
        print(f'\tPlease aim to save K{int((goal - actual) * (savings_percentage / 100))}')