#Checking if there are any users in a list
usernames = []
if usernames == []:
    print("You have no usernames, kindly add some names!")
AdminPaswd = input("Please enter your Admin Password: ")
if AdminPaswd == "admin":
    print("You are logged as an administrator")
else:
    print("Wrong password, try again after an hour")
#Adding users
while len(usernames) < 6:
    addingUsers = input("Kindly add usernames as an admin: ")
    usernames.append(addingUsers)
for username in usernames:
    print(f"{username.title()} has been successfully added")
print(f'\nHere is a summary of usernames which have been added:')
for username in usernames:
    print(f"{username.title()}")
print("You can log out now.")

