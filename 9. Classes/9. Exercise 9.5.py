#Creating a class about users
class User:
    def __init__(self, first_name, last_name, age, email, department):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.department = department
        self.login_attempts = 0

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

    #Increasing login attempts
    def increment_login_attempts(self):
        while self.login_attempts < 3:
            login = int(input("\n\tEnter your login number: "))
            self.login_attempts += 1
            print(f'\tYou have {self.login_attempts} login attempts, remaining with {3-self.login_attempts} attempts.')
            if self.login_attempts == 3:
                print(f'\n\tYou have {self.login_attempts} login attempts. You do not have any attempts')
        print("\tKindly reset the login attempts to 0")
    #Resetting login attempts
    def reset_login_attempts(self):
        self.login_attempts = 3
        reset_attempts = input("\n\tDo you want to reset? (yes/no): ")
        if reset_attempts == 'yes':
            print(f'\n\tCongrats you have {self.login_attempts} login attempts again.')
        else:
            print(f'\n\tSorry, your login attempts reset failed. Try again later!')

#creating instances and thereafter calling them
user1 = User("Givious", "Haluse", 35, "gflixes@gmail.com", "Computer")
user2 = User("Rose", "Zulu", 20, "zulur@gmail.com", "Health")
user3 = User("Sunwell", "Haluse", 32, "givioushaluse@gmail.com", "Computer")

#Calling the method to show how login attempts are increasing
user1.increment_login_attempts()

#Calling a method to reset the number of attempts
user1.reset_login_attempts()
