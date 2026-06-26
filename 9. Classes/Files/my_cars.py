#In this file we will import two modules containing the classes for the
#car, battery and electric car
from car_only_module import Car
from battery_electriccar_module import ElectricCar

my_beetle = Car("volkswagen", "beetle", 2020)

#Describing the car
print(my_beetle.get_descriptive_name())
my_beetle.odometer_reading = 100
my_beetle.read_odometer()

#checking if it accepts gasoline or fule
my_beetle.fill_gasoline()

"""my BYD Electric car specifications and details"""
my_byd = ElectricCar("byd", "S", 2020)
print(my_byd.get_descriptive_name())
#checking the battery size
my_byd.battery.describe_battery()

#how far it can go with such batter power
my_byd.battery.get_range()
