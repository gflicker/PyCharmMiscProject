#Allowing users to add their names into a log book
start = True
while start:
    file_name = 'guest.txt'
    name = input("Enter your name (q to quit): ")

    if name == "q":
        start = False
        with open(file_name) as updated_guests:
            updated_list = updated_guests.read()
        print(f'Here is a list of all the guests: \n\t{updated_list}')

    else:
        with open(file_name, 'a') as update_guests:
            update_guests.write(name + "\n")
        print("Name successfully added!")
