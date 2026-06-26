#Input changing into integers and Modulo function for remainders
multipleOfTen = int(input("Kindly enter your number to see if it's a multiple of 10 or not: "))
if multipleOfTen % 10 == 0:
    print(f'{multipleOfTen} is a multiple of 10.')
else:
    print(f'{multipleOfTen} is not a multiple of 10 because the remainder is {multipleOfTen % 10}.')
print("Thanks for playing the game.")