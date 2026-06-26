# A function which accepts two parameters: a city name and a country name.
def city_country(city, country, population = ''):
    """Printing of a city and a country where that city is found"""
    if population:
        full_name = f'{city}, {country} -- Population: {population}'
    else:
        full_name = f'{city}, {country}'
    return full_name.title()