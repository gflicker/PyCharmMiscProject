#Raising numbers to the power 3 or cubes
for cube in range(1,10):
    # print(cube**3)
    cubed = cube ** 3
    print(cubed)
print("Thank you for playing the game!!!")
print("\nThe following result is from a "
      "list that has been comprehensed:")
cubedNumbers = [cube ** 3 for cube in range(1,10)]
print(cubedNumbers)
print("Thank you for playing the game!!!")