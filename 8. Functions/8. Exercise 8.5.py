#Parameters, cities and country
def describe_city(city_name="lusaka", country="zambia"):
    """Printing the description of the city and country"""
    print(f'{city_name.title()} is in {country.title()}')

#Calling the function using keyword arguments
describe_city()
describe_city(country="south africa", city_name="pretoria")
describe_city(city_name="tokyo", country="japan")