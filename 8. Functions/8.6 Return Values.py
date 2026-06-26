"""A function returning a formatted full name from the first and last name parameters"""
def get_formatted_name(first, last):
    """Return a full name, neatly formatted."""
    full_name = f'{first} {last}'
    return full_name.title()

student = get_formatted_name('john', 'doe')
print(f'Your name is {student}')