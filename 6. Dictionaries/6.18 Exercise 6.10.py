#Favorite numbers dictionary
favorite_numbers = {
    "sunwell":[1,3,6], "haggai":[0,3,4], "rose":[1], "givious":[7,17], "precious":[8,10]
}
for name, number in favorite_numbers.items():
    #print(f'{len(size)} items:  {size}')
    if (len(number) > 1):
        print(f'{name.title()}"s favorite numbers are: \t\n{number}')
    else:
        print(f'{name.title()}"s favorite number is: \t\n{number}')