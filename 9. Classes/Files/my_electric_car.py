#Importing the class ElectricCar from a car blue print module
from car_module import ElectricCar
#Creating an instance from this class
my_byd = ElectricCar('BYD', 'model s', 2019)

print(my_byd.get_descriptive_name())

my_byd.fill_gasoline()

#Calling the battery description method
my_byd.battery.describe_battery()

#Calling a method to see the range of the car proportional to the battery size
my_byd.battery.get_range()