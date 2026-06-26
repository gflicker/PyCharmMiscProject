"""Arguments that are using a key word doesn't matter the position"""

def description(name, skin_color):
    """Description of the person's appearance"""
    print(f'Your name is {name.title()} and your skin color is {skin_color}')

#Calling the function with positional arguments
description(name='caramel', skin_color='coffee brown')
"""A function can be called multiple times and doesnt matter what argument should come first"""
description(skin_color='brown', name='givious')
