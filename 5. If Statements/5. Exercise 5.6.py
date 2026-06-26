#Determing a person's stage of life
age = input("How old are you? ")
age = int(age)
if age < 2:
    print(f"You are a baby and you are {age} years old.")
elif age >=2 and age < 4:
    print(f"You are a toddler and you are {age} years old.")
elif age >= 4 and age < 13:
    print(f"You are a kid and you are {age} years old.")
elif age >= 13 and age < 20:
    print(f"You are a teenager, you are {age} years old.")
elif age >= 20 and age < 65:
    print(f"You are an adult, you are {age} years old.")
elif age >= 65:
    print(f"You are an elder, you are {age} years old.")
#The else block can be skipped or it can be option
print("Thanks for playing!")