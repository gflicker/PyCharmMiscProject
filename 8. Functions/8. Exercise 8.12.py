#A function which accepts more arguments
def my_siblings(*names):
    for name in names:
        print(f'{name.title()} is my sibling.')
#Calling a function
my_siblings("haggai", "sunwell", "kelving", "precious")