import json
"""Prompting the user to enter a new favorite number"""

filename = 'favorite_numbers.json'
#Prompting the user to enter their favorite number
favorite_number = input('Please enter your favorite number: ')
with open(filename, 'w') as f:
    json.dump(favorite_number, f)

"""Retrieving the favorite number"""
filename = 'favorite_numbers.json'
with open(filename) as f:
    favorite_number = json.load(f)
print(f'Your favorite number is {favorite_number}')