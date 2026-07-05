#Creating a list to show messages for different items
subjects = ["Mathematics", "Physics", "Programing"]
ranking_subject = int(input("Please choose your ranking: "))

if ranking_subject == 0:
    print(f'{subjects[ranking_subject]} is my favorite subject')
else:
    if ranking_subject == 1:
        print(f'{subjects[ranking_subject]} is my second favorite subject.')
    else:
        if ranking_subject == 2:
            print(f'{subjects[ranking_subject]} is my third favorite subject.')
        else:
            print('There is no favorite subject')
print("Thank you, we now know your subject")
print (subjects[ranking_subject])

