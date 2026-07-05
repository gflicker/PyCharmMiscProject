#When more if statements are needed
#Amusement park rates
age = int(input("What is your age? "))
if age < 4:
    addMissionFee = "$0"
elif age < 18: #we print the answer outside the if block instead
    #print("Your admission cost is $25. Please enjoy your stay!")
    addMissionFee = "$25"
#We can have a lot elif blocks in a program
elif age < 65:
    addMissionFee = "$40"
#Note that else is not a requirement, python can still execute without it
else:
    #print("Your admission cost is $40. Please enjoy your stay!")
    addMissionFee = "$20"
print(f'Your addmission cost is {addMissionFee}. Please enjoy you tour!!!')