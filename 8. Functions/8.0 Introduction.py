#Defining a function or creating a function
def personal_details():
    print("Hello kindly check if your details are correct.")
    name = input("Enter your first name: ")
    surname = input("Enter your surname: ")
    age = input("Enter your age: ")
    print(f'Your name is {name.upper()} {surname.upper()} '
          f'and you are {age} years old.')

#Calling the function we have defined
personal_details()