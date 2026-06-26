"""A function returning a formatted full name from the first and last name parameters"""
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f'{first_name} {middle_name} {last_name}'
    else:
        full_name = f'{first_name} {last_name}'
    return full_name.title()

student = get_formatted_name('givious', 'haluse')
print(f'Your name is {student}')
#When a middle name is given
student= get_formatted_name(middle_name='caramel', last_name='zulu', first_name='rose')
print(f'Your name is {student}')