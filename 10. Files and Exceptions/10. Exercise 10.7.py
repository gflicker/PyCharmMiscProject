#Printing VallueError exception
start = True
while start:
    print("\nEnter two numbers then I will give you the sum")
    try:
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter second number: "))

    except ValueError:
        print("Sorry, you can only enter numbers not text.")
    else:
        answer = first_number + second_number
        print(f'The sum of {first_number} and '
          f'{second_number} is {answer}')

