#Checking if one is eligible to vote or note
age = input('How old are you? ')
age = int(age)
if age >= 18:
    print(f'You are {age} years old. You are eligible to vote.'
          f'\nCongratulations!!!')
    registered = input('Have you registered to vote yet? ')
    registered.lower()
    if registered == "yes":
        print("Great! Keep your voter's card safe, don't share it \n"
              "with anyone or sell it, its a crime.")
        print("Make sure to verify your registration with ECZ.")
    else:
        print("Kindly go and register to vote in the 2026 General Elections")
else:
    remainder = 18 - age
    print(f'Please wait for {remainder} years to qualify to vote')


