#Counting common words in a file
#Counting a number of times a word appears in the file that has been opened.
filename = 'paradox.txt'
with open(filename) as file:
    lines = file.read()
print(lines.lower().count('the '))