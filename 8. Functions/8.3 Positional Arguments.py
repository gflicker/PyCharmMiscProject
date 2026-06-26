"""Arguments that are using their index position or to be written following position"""

def description(name, skin_color):
    """Description of the person's appearance"""
    print(f'Your name is {name.title()} and your skin color is {skin_color}')

#Calling the function with positional arguments
description('caramel', 'coffee brown')
"""A function can be called multiple times"""
description('givious', 'brown')
