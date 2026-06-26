#Creating a class about users
class User:
    def __init__(self, first_name, last_name, age, email, department):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.department = department

    # A method to print all this information
    def describe_user(self):
        print(f'\tHere are the details of {self.first_name} {self.last_name}')
        print(f'\tName: {self.first_name} {self.last_name} '
              f'\n\tAge: {self.age} '
              f'\n\tEmail: {self.email} '
              f'\n\tDepartment: {self.department}')

    #Creating a method that greets the user
    def greet_user(self):
        print(f'\n\tHello {self.first_name} {self.last_name}, you are in the database.')
#creating instances and thereafter calling them
user1 = User("Givious", "Haluse", 35, "gflixes@gmail.com", "Computer")
user2 = User("Rose", "Zulu", 20, "zulur@gmail.com", "Health")
user3 = User("Sunwell", "Haluse", 32, "givioushaluse@gmail.com", "Computer")

#Calling each using methods.
user1.describe_user()
user1.greet_user()

#User2
user2.greet_user()
user2.describe_user()

#user3
user3.greet_user()
user3.describe_user()

