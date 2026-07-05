#Analyzing text files in an entire book or where alot of text block is involved
#Building a list of words from a string
#Creating a function to use to analyze alot of books

def count_words(filename):
    """Counting the approximate number of words in a file."""
    try:
        with open(filename, encoding = 'utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File {filename} does not exist.")
    else:
        words = content.split()
        num_words = len(words)
        print(f'The file {filename} has {num_words} words.')

filename = 'learn_python.txt'
count_words(filename)

#Using a list to get the file name in order to create a loop
filenames = [
    'alice.txt',
    'bob.txt',
    'guest.txt',
    'pi_digits.txt',
    'programming.txt',
]

#Looping through all the files to count number of words
for filename in filenames:
    count_words(filename)