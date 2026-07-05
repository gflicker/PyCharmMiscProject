#Prompting users to state reasons why they like programming
print("Welcome this Programming Poll. Please give your sincere reasons.")
start = True
while start:
    filename = 'rose.txt'
    reason = input("Why do you like programming? (q to quit): ")


    #Exiting the loop
    if reason == "q":
        start = False
        with open(filename) as reasons:
            updated_reasons = reasons.read()
        print(f'\nHere are your reasons: {updated_reasons}')

    else:
        with open(filename, 'a') as update_reasons:
            update_reasons.write(reason + '\n')