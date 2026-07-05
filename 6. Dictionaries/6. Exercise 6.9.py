#My favorite places dictionaries
favorite_places = {
    "rose":{
        "name":"lusaka", "province":"lusaka", "capital":"lusaka"
    },
    "givious":{
        "name":"livingstone", "province":"southern", "capital":"choma"
    },
    "sunwell":{
        "name":"mazabuka", "province":"southern", "capital":"choma"
    },
    "kelvin":{
        "name":"solwezi", "province":"Northwestern", "capital":"solwezi"
    },
}
print("Here is a list of my friends and there favorite places")
for person, place in favorite_places.items():
    print(f'\t{person.title()} loves {place["name"].title()} of {place["province"].title()} Province 'f'whose provincial capital is {place["capital"].title()}')