#Reading files
def files(filename):
    try:
        with open(filename) as file:
            content = file.read()
    except FileNotFoundError:
        print(f'Sorry, the file {filename} does not exist.')
    else:
        print(f'')
filenames = [
    'cats.txt', 'dogs.txt', 'givious.txt'
]
for filename in filenames:
    files(filename)