#while loops ina function
"""A function returning a formatted full name from the first and last name parameters"""
def get_formatted_name(first, last):
    """Return a full name, neatly formatted."""
    full_name = f'{first} {last}'
    return full_name.title()

#infinite loop!
while True:
    print("\nPlease enter your first name and last name")
    #Stopping the loop whenever needed
    print("enter 'q' any time to quit")
    first_name = input("First name: ")
    if first_name == 'q':
        break
    last_name = input("Last name: ")
    if last_name == 'q':
        break
    formatted_name = get_formatted_name(first_name, last_name)
    print(f"\nYour name is {formatted_name}")