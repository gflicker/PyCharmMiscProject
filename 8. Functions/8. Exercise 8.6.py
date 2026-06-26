def city_country(city, country):
    """Return a city country name."""
    full_name = f'{city}, {country}'
    return full_name.title()

ZM = city_country('Lusaka', 'zambia')
CE = city_country('cairo', 'egypt')
AE = city_country('Addis Ababa', 'ethiopia')
print(ZM)
print(CE)
print(AE)