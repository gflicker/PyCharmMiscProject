#Making a prompt that ends only when a while loop condition is met
Vacation = {}
start = True
while start:
    name = input('What is your name? ')
    vacation_place = input('If you could visit one place in the world,'
                           'where would you go? ')
    Vacation[name] = vacation_place
    #The code to end the infinite while loop
    proceed = input('Would you like to proceed? (yes/no) ')
    if proceed == 'no':
        start = False

for name, place in Vacation.items():
    print(f'\t{name} would like to visit {place}')