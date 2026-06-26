#How a class can inherit another class
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

        def update_odometer(self, mileage):
            if mileage >= self.odometer_reading:
                self.odometer_reading = mileage
            else:
                print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def fill_gasoline(self):
        """Filling the tank"""
        print("You have refuelled your car with 10lts of gasoline.")

#A new class which is called a child is inheriting attributes from the parent class
class ElectricCar(Car):
    """Represent the aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year) #Initializing Car as a parent class.
        #Adding new attributes to the child class
        self.battery_size = 75 #Defining an attribute outside the init method

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size} battery.")

    #Overriding a method which is in the parent class fill_gasoline as electric dont have fuel tanks
    def fill_gasoline(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank but a battery only.")

#Getting all attributes and methods from the parent class 'Car'
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

#Battery description
my_tesla.describe_battery()
my_tesla.fill_gasoline()