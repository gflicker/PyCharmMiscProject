#Reading external files by relative paths or absolute path.
"""Looping the program three times"""
print("This code below loops the program 3 times.")
i = 0
while i < 3:
    i += 1
    filename = 'learn_python.txt' #Assign it to a variable for easy manipulation
    with open(filename) as python_learning:
        reading_file = python_learning.read()
    print(f'Here is what is contained in the filename:\n{reading_file}')

print("Running the code once")
filename = 'learn_python.txt' #Assign it to a variable for easy manipulation
with open(filename) as python_learning:
    reading_file = python_learning.read()
print(f'Here is what is contained in the filename:\n{reading_file}')

#Reading line by line
print("PRINTING LINES IN A TEXT FILE INTO A LIST")
filename = 'E:\\Studio 1\\Videos\\Python\\Crash Course\\10. Files and Exceptions\\learn_python.txt'
with open(filename) as file_list:
    list_lines = file_list.readlines()
print(list_lines)

#Firstly reading each line and replace pythong with C++
print("\nREPLACING WORDS IN THE FILE USING THE REPLACE ATTRIBUTE")
filename = 'learn_python.txt'
with open(filename) as replacing_word:
    list_line = replacing_word.read()
    for line in list_line:
        list_line = list_line.replace('python', 'C++')
    print(list_line)