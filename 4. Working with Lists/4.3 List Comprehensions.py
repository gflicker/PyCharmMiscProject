#Having a number of lines of code in one
#This means avoiding more variables or temporarily
#The following example shows lines of codes without simplifying them
#Generating cubes of numbers from 1-10
cubes = []
for cube in range(1, 11):
    cubeRoot = cube ** 3
    cubes.append(cubeRoot)
print(f'The cubes of the numbers is:\n\t {cubes}')
#Shorten codes or codes in one line
cubes = [cube**3 for cube in range(1, 11)]
print(f'\n\nThis is from the abbreviated codes. Same results \n'
      f'The cubes of the numbers is:\n\t {cubes}')