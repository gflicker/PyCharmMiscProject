#Slicing is all about accessing elements in a range of indices
Players = ["Sala", "Gomez", "Ekitike", "Allison", "Szobosilai", "Virgil"]
print(f'These are the first three players: \n{Players[0:3]}')

print(f'These are the last two players: \n{Players[-3:-1]}')
print(f'When you omit the starting index it will output till the stop index:'
      f'\n{Players[:2]}')
print(Players[0:1:4])

#The list where the three option slice is used in lists
print("This is an output where a third argument is used in "
      "\na slice of a list like [0:18:2. This tells python to print"
      "\nnumbers from 0 to 18 and each time to skip 2 numbers."
      "\nSo the list will be like 0, 2, 4, 6......")
beautifulNumbers = []
for number in range(1,20):
    beautifulNumbers.append(number)
print(beautifulNumbers[1:20:2])