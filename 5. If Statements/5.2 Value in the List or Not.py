#Checking whether an item is in the list or not
requested_foods = ["mushrooms", "onions", "chicken"]
if "mushrooms" in requested_foods:
    print("Congratulations! You ordered mushrooms!\n")
#Adding users to the list
users_list = ["givious", "sunwell", "haggai","kelvin", "precious", "tristan"]
adding_user = input("Add a username: ")
adding_user = adding_user.lower()
#Checking to see if the user already exists
if adding_user in users_list:
    print("Sorry username already taken, kindly choose another.")
else:
    users_list.insert(0 , adding_user)
    print(f'A new username {adding_user.title()} was added to the list.')
numberOfUsers = len(users_list)
print(f'You have {numberOfUsers} users registered.')