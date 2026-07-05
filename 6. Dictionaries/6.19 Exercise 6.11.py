#Dictionary of cities
cities = {
    "ndola": {"country": "zambia", "population": "200", "fact": "the cleanest town in Zambia."},
    "durban": {"country": "South Africa", "population": "300", "fact": "the coldest city in SA"},
    "cairo":{"country": "egypt", "population": "900", "fact": "the city with beautiful historical sites" },
}
for city in cities:
    print(f'Here is the information about {city.title()}:')
    for name, info in cities[city].items():
       print(f'\t{name.title()}: {info.title()}')