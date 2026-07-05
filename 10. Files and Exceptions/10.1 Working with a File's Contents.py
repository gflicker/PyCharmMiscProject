#Reading a text file
filename = "pi_digits.txt"
with open(filename) as file_content:
    lines = file_content.readlines()

#Want to concatenate the lines into one
pi_string = ''
for line in lines:
    pi_string += line.strip() #Concatenating lines

print(pi_string)
print(f'There are {len(pi_string)} characters in pi_string') #Number of characters in a string

#Making a text file and what to do with large files
filename = "pi_digits.txt"
with open(filename) as file_object:
    line = file_object.readline()
    pi_string = '3.14159265450000000000000000000333221154687778876869595858'
    for line in file_object:
        pi_string += line.strip()

    print(f'{pi_string[:52]}. These are {len(pi_string[:52])} characters in pi_string')
    print(f'There are {len(pi_string)} characters in pi_string.')