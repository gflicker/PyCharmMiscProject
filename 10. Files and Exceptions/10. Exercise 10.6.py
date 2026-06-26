#Printing VallueError exception
print("Enter two numbers then I will give you the sum")
try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter second number: "))

    answer = first_number + second_number
except ValueError:
    print("Sorry, you can only enter numbers not text.")
else:
    print(f'The sum of {first_number} and '
          f'{second_number} is {answer}')
