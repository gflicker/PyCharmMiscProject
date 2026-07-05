#Passing a list into a function as a parameter or an argument
#A function which greets users which pics users from a list passed into a function
def greet_user(names):
    """Printing a simple greeting to each user in the list."""
    for name in names:
        msg = f'Hello, {name.title()}!'
        print(msg)

#Making a list to be passed to be passed as an argument
usernames = ["Caramel", "Patricia", "Precious", "Haggai", "Estina"]
greet_user(usernames)