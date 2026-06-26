#The program will keep running without crashing by skipping the error block
print("Give me two numbers, and I will divide them.")
print("Enter 'q' to quit.")

start = True
while start:
    first_number = input("\nEnter first number: ")
    if first_number == 'q':
        break
    second_number = input("Enter second number: ")
    if second_number == 'q':
        break
    #Placing the try-except block immediately before the line that is likely to produce the error
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by zero")
    
    else:
        print(answer)