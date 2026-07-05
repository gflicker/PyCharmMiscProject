#Making a class about a restaurant
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    #Creating a method (function) describing the restaurant
    def describe_restaurant(self):
        print(f'Here at {self.restaurant_name} we serve you the best {self.cuisine_type} cuisine.')

    #Creating a method (function) highlighting that our restaurant is open
    def open_restaurant(self):
        print(f'{self.restaurant_name} is now open. Come and enjoy great meals. ')

#Creating objects (variables) to call the methods under this class
my_res = Restaurant("Betty's Foods", "Swiss")
my_res.describe_restaurant()
my_res.open_restaurant()

#Three instances and calling the describe_restaurant method on each instance
patience = Restaurant("Patience's Food Palace", "French")
chanda = Restaurant("Chanda's Food Hub", "Spanish")
mirriam = Restaurant("Mirriam's Restaurant", "American")

#Calling a method on each
patience.describe_restaurant()
chanda.describe_restaurant()
mirriam.describe_restaurant()