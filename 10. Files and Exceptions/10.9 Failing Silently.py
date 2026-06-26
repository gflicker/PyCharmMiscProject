#Errors being silently handled using exceptions
def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass #Not giving any warning about the error
    else:
        words = contents.split()
        num_words = len(words)
        print(f'The file {filename} has about {num_words} words.')

filenames = ['guest.txt', 'learn_python.txt',
             'programming.txt', 'rose.txt', 'givious.txt']
#Looping through the list of files to count words
for filename in filenames:
    count_words(filename)