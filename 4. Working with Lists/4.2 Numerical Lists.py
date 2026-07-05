#Printing a series of number
SetofNumbers = []
for value in range(1,5): #Off by one rule only prints up to 4
    print(value)
    #SetofNumbers.append(value)
#print(SetofNumbers)


#Printing even numbers
even_numbers = list(range(2,13,2))
print(even_numbers)

#Simple Statistics with a List of Numbers
# Using functions such as:
# 1. Min() for minimum
# 2. Max() for maximum
# 3. sum() for summing up numbers
numbers = []
for number in range(1,101):
    numbers.append(number)
#Smallest number in the list generated:
smallest = min(numbers)
print(f'The smallest number is: {smallest}')

#Largest number in the list generated:
largest = max(numbers)
print(f'The largest number is: {largest}')

#Summing them up
adding_numbers = sum(numbers)
print(f'The sum of the numbers is:\n\t Total: {adding_numbers}')