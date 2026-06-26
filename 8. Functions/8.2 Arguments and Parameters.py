#A parameter is more like the variable that tells the users what to pass in the fucntion
#An argument is what has been passed into a function to be called
#Passing Information to a Function
username = input("Enter your username: ")
"""Here the username is a parameter"""
def personal_details(username):
    print("Hello kindly check if your details are correct.")
    name = input("Enter your first name: ")
    surname = input("Enter your surname: ")
    age = input("Enter your age: ")
    print(f'The name associated to the username {username.lower()} is {name.upper()} {surname.upper()} '
          f'and {age} years old.')

#Calling the function we have defined
"""Here the username is an argument as it has been passed into the call function"""
personal_details(username)
