#Generating a list of odd numbers
for number in range(1,10,1):
    odd_number = (number * 2) - 1
    print(odd_number)
print("Thank you!!!")

#Another way by using a List Comprehension
print("\nThis list is from a list comprehension code.")
OddNumbers = [(number * 2) - 1 for number in range(1,10,1)]
print(OddNumbers)

#Multiples of 3
print("\n Here are the multiples of three:")
for number in range(3,30,3):
    print(number)
print("Thank you for playing the game!!!")
