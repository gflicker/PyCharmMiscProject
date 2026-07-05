#Removing all instances of values in a list using a while loop
pets = [
    'dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbi', 'cat'
]

while 'cat' in pets:
    pets.remove('cat')
print(pets)