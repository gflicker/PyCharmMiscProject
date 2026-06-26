#Ordinal Numbers-Indicating position, e.g 1st, 3rd
Ordinal_numbers =  range(1,10)
for number in Ordinal_numbers:
    if number == 1:
        print(f'\t{number}st')
    elif number == 2:
        print(f'\t{number}nd')
    elif number == 3:
        print(f'\t{number}rd')
    else:
        print(f'\t{number}th')
print("Thank you for playing the game.")