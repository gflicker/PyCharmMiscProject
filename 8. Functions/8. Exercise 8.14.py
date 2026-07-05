#Passing arbitrary keyvalue pairs and mixing with positional arguments
def favorite_car(maker, model_name, **car_info):
    car_info['Manufacturer'] = maker
    car_info['Model'] = model_name
    return car_info

car = favorite_car('Toyota', 'D4d', drive="4WD", tank=1.8)
print(car)