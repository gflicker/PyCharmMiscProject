#Using default parameters
def make_shirt(size='Large', message="I love Python"):
    """A function with only one positional argument which is size"""
    print(f'Kindly make a shirt with {size} size and a message which '
          f'says {message}. ')

make_shirt()
"""Calling a function using keyword argument"""
make_shirt(size='Medium')
"""Calling a function using keyword argument"""
make_shirt(size='small', message="I can do it")
