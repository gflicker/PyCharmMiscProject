#Checking if the username already exists
current_users = ["Rose", "John", "Joey", "Haggai", "Jack", "Estina"]
new_users = ["Caramel", "Givious", "Rose", "Sunwell", "Estina", "Precious"]
for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user.title()} is already taken, kindly enter a new one.")
        new_users.remove(new_user)
        new_one = input("Enter a different username: ")
        new_users.append(new_one)
    else:
        print(f"{new_user.title()} has been added to the directory.")
#Printing a list of all new users that have been added
print("Here is a summary of your current users:")
all_users = current_users + new_users #Concatinating lists
all_users.sort()
for all_user in all_users:
    #Adding new_users to the current users in the directory.
    print(all_user)
print(f"Directory successfully updated.You have {len(all_users)} users.")