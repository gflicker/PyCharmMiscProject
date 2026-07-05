#Looping through dictionaries in a list
pets = [
    {"breed": "Germany shepherd", "Owner": "Haggai", "Age": 4},
    {"breed": "Bull dog", "Owner": "Kelvin", "Age": 2},
    {"breed": "African", "Owner": "Givious", "Age": 7},
    {"breed": "Rotweillers", "Owner": "Sunwell", "Age": 3},
]

print("Here are the different types of breeds we have:")
for pet in pets:
    print(f"\t{pet['breed']}")
print("\nHere are full details about these pets:")
for pet in pets:
    for owner, age in pet.items():
        print(f"\t{owner.title()}:           {age}")