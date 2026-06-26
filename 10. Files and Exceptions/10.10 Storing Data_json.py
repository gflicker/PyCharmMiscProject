#Storing data into a json file
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f) #f represents the filename the numbers should be dumped to

"""Now we want to load back the numbers into the program even after we quit it"""
with open(filename) as f:
    numbers = json.load(f)
print(numbers)