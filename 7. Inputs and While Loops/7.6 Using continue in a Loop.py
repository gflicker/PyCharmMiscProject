#Making the loop returning to the beginning instead of quiting
print("Here are odd numbers which are less than 10.")
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(f'\t{current_number} ')