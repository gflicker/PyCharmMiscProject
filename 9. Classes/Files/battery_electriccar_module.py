#The car class is needed as a parent class or as a superclass to the child class
#which is electric car
from car_only_module import Car

class Battery:
    def __init__(self, battery_size = 60):
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-KWh battery.")

    #A method that determines how far a car can travel looking the size of the battery
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            ranges = 260
            print(f"This car has can go about {ranges} miles on it.")
        elif self.battery_size == 100:
            ranges = 315
            print(f'This car can go about {ranges} miles on it.')
        else:
            print(f'Your battery is low, please recharge it.')

#A new class which is called a child is inheriting attributes from the parent class
class ElectricCar(Car):
    """Represent the aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year) #Initializing Car as a parent class.
        #Adding new attributes to the child class
        self.battery = Battery() #Defining an attribute outside the init method

    #Overriding a method which is in the parent class fill_gasoline as electric dont have fuel tanks
    def fill_gasoline(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank but a battery only.")