#Introducing if statements
cars = ["audi", "subaru", "mazda", "toyota", "isuzu", "honda", "bmw"]
#looping through until the condition is met
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())