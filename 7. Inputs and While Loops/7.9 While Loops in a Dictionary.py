#Filling a dictionary with user input
responses = {}
#Set a flag to indicate that the polling is active
polling_active = True
while polling_active:
    #Prompt the person's name and response
    name = input('What is your name? ')
    response = input('What is your favourite subject? ')

    #Storing the response in the dictionary
    responses[name] = response

    #Find out if anyone else is going to take the poll.
    repeat = input('Would you like to let another person respond? (yes/no) ')
    if repeat == 'no':
        polling_active = False
#Polling is complete. Show the results.
print(f'\n----------------Poll Results----------------')
for name, response in responses.items():
    print(f"{name}'s favorite subject is {response}.")