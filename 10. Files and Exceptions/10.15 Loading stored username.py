#Separating the functions for the one to load the stored data and the one for retrieving
import json
def get_stored_username():
    """Get a stored username"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompting the user to enter a new username"""
    username = input("What is your username? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user"""
    username = get_stored_username()
    if username:
        print(f'Welcome back {username}!')
    else:
        username = get_stored_username()
        print(f'We will remember you when you coe back {username}!')

greet_user()