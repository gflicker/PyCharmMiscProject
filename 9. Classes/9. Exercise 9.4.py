class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
    #Creating a method (function) describing the restaurant
    def describe_restaurant(self):
        print(f'Here at {self.restaurant_name} we serve you the best {self.cuisine_type} cuisine.')

    #Creating a method (function) highlighting that our restaurant is open
    def open_restaurant(self):
        print(f'{self.restaurant_name} is now open. Come and enjoy great meals. ')
    #Method for a number of customers served
    def customers_served(self):
        print(f'We have {self.number_served} customers served at home. ')

    def update_number_served(self):
        self.number_served = 13
        if self.number_served == 1:
            print(f'{self.restaurant_name} has served {self.number_served} customer.')
        else:
            print(f'{self.restaurant_name} has served {self.number_served} customers.')

    #A method to increment number of served customers from the initial value
    def increment_number_served(self):
        self.number_served += 40
        print(f'{self.restaurant_name} has served {self.number_served} customers.')

#Printing number of customers served
restaurant = Restaurant('Chanda Food Hub', 'Mango')
restaurant.customers_served()

#Showing the change in the number of customers served
restaurant.update_number_served()

#Increasing the number of customers as they come
restaurant.increment_number_served()