#Executing a code until a certain number of loops
current_number = 1
while current_number < 10:
    current_number += 2
    #print(current_number)
    if current_number % 2 == 0:
        print(f'{current_number} is even')

    else:
        print(f'{current_number} is odd')
