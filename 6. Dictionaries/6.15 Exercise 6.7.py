mypeople = [
    {
        "name": "rose",
        "status": "engaged to Givious",
        "age": 20,
        "town": "lusaka"
    },
    {
        "name": "sunwell",
        "status": "married to Nachilila",
        "age": 33,
        "town": "mazabuka"
    },
    {
        "name": "haggai",
        "status": "married to Estina",
        "age": 28,
        "town": "lusaka"
    }
]

print("These are my people:")
for people in mypeople:
    print(f'\t{people["name"].title()} is {people["status"]}.')