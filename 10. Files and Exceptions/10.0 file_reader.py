#Reading the content found in a certain file
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
print(contents)

#Absolute paths
print("\nThis output is from an absolute path for the file being ready")
file_path = 'C:\\Users\\USER\\PyCharmMiscProject\\10. Files and Exceptions\\pi_digits.txt'
with open(file_path) as file_object:
    contents = file_object.read()
print(contents)

#Reading a file line by line
filename = 'pi_digits.txt'
print("\nThis is an output from reading the file line by line")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip()) # rstrip helps remove extra lines after each line

#Making a List of lines from a file
print("\nMaking a list of lines from a file")
filename = 'pi_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

