#Passing Information to a Function
username = input("Please enter your username: ")

def personal_details(username):
    print("Hello kindly check if your details are correct.")
    name = input("Enter your first name: ")
    surname = input("Enter your surname: ")
    age = input("Enter your age: ")
    print(f'The name associated to the username {username} is {name.upper()} {surname.upper()} '
          f'and {age} years old.')
#Calling the function we have defined
personal_details(username)
