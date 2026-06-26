#Note: If there's only one item in a tuple, add a trailing comma
#Looping through tuples, same as in a list
dimensions = (10, 15, 4)
for number in dimensions:
    print(number)

#Writing over a Tuple by assigning it to new values
dimensions = (10, 15, 4)
print("This is the original dimensions:")
for number in dimensions:
    print(number)
#The writing over a Tuple
dimensions = (100, 150, 40)
print("\nThis is a modified dimensions:")
for number in dimensions:
    print(number)
#No errors because reassigning a variable is valid