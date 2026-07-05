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

#Separate class for privileges
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    #Creating a method for privileges
    def show_privileges(self):
        print('The following are some of the privileges you have as an Admin user')
        for privilege in self.privileges:
            print(f'\t- {privilege.capitalize()}')

#A class for an admin user
class Admin(User):
    def __init__(self, first_name, last_name, age, email, department):
        super().__init__(first_name, last_name, age, email, department)
        self.privileges = Privileges([
            "can add post", "can delete post", "can ban user"
        ])

myadmin = Admin("first", "last", "age", "email", "department")
myadmin.privileges.show_privileges()




