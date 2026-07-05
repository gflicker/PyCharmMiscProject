#Here we are importing a single class from a file name car_blue_print
#This is about a car blue-print
from car_module import Car

#Creating an instance from the class called Car from the file car blue-print
my_new_car = Car('land cruiser', "prado", 2015)

print(my_new_car.get_descriptive_name())

my_new_car.fill_gasoline()
my_new_car.odometer_reading = 50
my_new_car.read_odometer()
my_new_car.increment_odometer(23)
