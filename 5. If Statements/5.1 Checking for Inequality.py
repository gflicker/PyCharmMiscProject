#Comparing two things that are not equal
requested_foods = input("What are you ordering? ")
if requested_foods != "chicken":
    print("Kindly hold the chicken for now!")
print(f'{requested_foods.title()} is the requested food.\n')
#Numerical comparisons
print("Welcome to the Examination Results Program")
studentScore = int(input("What is the pass mark? "))
if studentScore != 40:
    print("Sorry, that is not correct. Try again.")
else:
    print(f'You are correct The pass mark is {studentScore}')
print("Thank you for playing!")
