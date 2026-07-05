#List of guests for dinner
dinner_lists = ["Haggai", "Rose", "Nachie", "Sunwell", "Metreny", "James", "Hellen"]
write_invited = int(input("Who is invited?: "))
absent = int(input("Who is not attending?: "))
print(f'You have invited {dinner_lists[write_invited]} for dinner.')
#Those who won't attend
#absent = int(input("Who is not attending? "))
not_attending = dinner_lists.pop(absent)
if absent == 0:
    print(f'Unfortunately, {dinner_lists[absent]} will not make it.')
else:
    if absent == 1:
        print(f'Sorry, {dinner_lists[absent]} will not make it.')
    else:
        if absent == 1:
            print(f'Sorry {dinner_lists[absent]} will not make it.')
        else:
            if absent == 2:
                print(f'Sorry {dinner_lists[absent]} will not make it.')
            else:
                if absent == 3:
                    print(f'Sorry {dinner_lists[absent]} will not make it.')
                else:
                    if absent == 4:
                        print(f'Sorry {dinner_lists[absent]} will not make it.')
                    else: print("Your input is invalid, try again.")
print("Thank you for your message, Hope next time you will show up")
#Replacing one who will not attend
del dinner_lists[absent]
print(f'You are invited: {dinner_lists}')

#Planned to invite more guests
dinner_lists.insert(0, "Kelvin")
dinner_lists.insert(3, "Lilly")
dinner_lists.append("Enock")
print("The following are the confirmed dinner guests.")
print(dinner_lists)

#Only discovered that there are few tables.
First = int(input("Cancelled invitation: "))
dinner_lists.pop(First)
print(f'Sorry {dinner_lists[First]} we have cancelled the invitation.')

Second = int(input("Cancelled invitation: "))
dinner_lists.pop(Second)
print(f'Sorry {dinner_lists[Second]} we have cancelled the invitation.')

Third = int(input("Cancelled invitation: "))
dinner_lists.pop(Third)
print(f'Sorry {dinner_lists[Third]} we have cancelled the invitation.')

Fourth = int(input("Cancelled invitation: "))
dinner_lists.pop(Fourth)
print(f'Sorry {dinner_lists[Fourth]} we have cancelled the invitation.')

#Lets see how many guests are remaining
print(f'We have only managed to accomodate the following: \n{dinner_lists}')