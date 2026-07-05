#Reading files
def files(filename):
    try:
        with open(filename) as file:
            content = file.read()
    except FileNotFoundError:
        pass
    else:
        print(f'\n{content}')
filenames = [
    'cats.txt', 'dogs.txt', 'givious.txt'
]
for filename in filenames:
    files(filename)