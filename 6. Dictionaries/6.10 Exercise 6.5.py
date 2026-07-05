#Looping through a dictionary of Rivers
major_rivers = {
    "Zambezi": "Zambia and Zimbabwe",
    "Nile": "Egypt", "Congo":
        "Congo, The Democratic Republic of the Congo"}
print("Major Rivers in Africa and Countries they run through")
for river, country in major_rivers.items():
     print(f'\t{river} river runs through {country}')
#Printing names of the Rivers only
print("\nHere are the names of major rivers:")
for rivers in major_rivers.keys():
    print(f'\t{rivers} River')
#Printing countries where these rivers run through
print("\nHere are the names of countries of these major rivers:")
for country in major_rivers.values():
    print(f'\t{country}')