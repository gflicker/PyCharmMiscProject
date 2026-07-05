#Using a while loop with Lists
#Starting with users that need to be verified and an empty list
#to hold confirmed users.
unconfirmed_users = [
    "alice", "rose", "sunwell", 'estina'
]
confirmed_users = []
#Verifying users and moving them to the confirmed list
while unconfirmed_users:
    current_user = unconfirmed_users.pop()#removing them from unconfirmed

    print(f'Verifying user: {current_user.title()}')
    confirmed_users.append(current_user)

    #Displaying all confirmed users.
print(f'\nThe following users were confirmed:')
for confirmed_user in confirmed_users:
    print(f'\t{confirmed_user.title()}')
