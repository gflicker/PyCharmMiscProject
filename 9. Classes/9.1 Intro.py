#Creating an object for a dog, then add other behaviors of a dog.
class Dog:
    """Creating a simple model of a dog"""
    def __init__(self, name, age):
        """Initializing an instance of a dog"""
        self.name = name
        self.age = age
    """Adding a new instance of a dog or behaviors/properties"""
    def sit(self):
        """Simulating a dog sitting"""
        print(f'{self.name} is now sitting.')
    """Another instance of a dog or behaviors/properties done by creating a function"""
    def roll_over(self):
        """Simulating a dog roll over in response to a command"""
        print(f'{self.name} rolled over!')

#Making an instance
my_dog = Dog("Leo", 3)
print(f'My dog is {my_dog.name} and its {my_dog.age} years old')

#Calling methods or behaviors of a dog
my_dog.sit()
my_dog.roll_over()
