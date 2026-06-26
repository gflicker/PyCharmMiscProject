#Expenses categories
def categories(each_category):
    if "rent" in each_category:
        print(f'Here is a summary of Fundamentals Budget')
    elif "clothing" in each_category:
        print(f'Here is a summary of Recreaction Budget')
    else:
        print(f'Here is a summary of Savings')
    for key, value in each_category.items():
        print(f'\t{key.title()}: {value}')
