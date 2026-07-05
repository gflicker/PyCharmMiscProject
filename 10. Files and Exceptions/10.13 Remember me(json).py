#Using json.dump and json.load to write a simple program to save and retrieve names
# Firstly we will load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
import json

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your username? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f'We will remember your username, {username}!')
else:
    print(f'Welcome back, {username}!')