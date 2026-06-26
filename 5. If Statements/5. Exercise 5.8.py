#A program to record users in a database
usernames = ["admin", "sunwell","rositta", "unity", "haggai"]
for name in usernames:
    if name == "admin":
        print(f'Hello {name.title()}, would you like to see a status report?')
    else: print(f'Hello {name.title()}, thanks for logging in again.!')
print("Please beware of scammers online!!!!")