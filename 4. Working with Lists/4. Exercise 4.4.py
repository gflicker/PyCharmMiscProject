#list of numbers from 1 to 1000000
OneMillion = list(range(1,1000001))
print(OneMillion)

#Another method
One_million = []
for number in range(1,1000001):
    One_million.append(number)
print(One_million)
#Exercise 4.5 combine with Exercise 4.4
#smallest number
smallest = min(One_million)
print(f'The smallest number is:\n\t Smallest: {smallest}')
#Largest number
Largest = max(One_million)
print(f'\nThe Largest number is:\n\t Smallest: {Largest}')

#Sum of the list
addition = sum(One_million)
print(f'\nThe sum of the list is:\n\t Sum: {addition}')
print("Thanks for playing this game. Goodbye")