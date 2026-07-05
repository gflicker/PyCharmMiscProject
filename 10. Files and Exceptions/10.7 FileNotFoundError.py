#Handling errors to do with a file that might seem as if it is missing
filename = 'alice.txt'
try:
    with open(filename, encoding='utf-8') as file:
        content = file.read()
except FileNotFoundError:
    print(f' Sorry, the file {filename} does not exist.')

#Using the split function to list number of words in a string
else:
    #count the approximate number of words in the file
    words = content.split()
    num_words = len(words)
    print(f'The file {filename} has {num_words} words.')