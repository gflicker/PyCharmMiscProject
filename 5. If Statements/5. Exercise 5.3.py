#Using if statements
#Check if you've earned any points
alien_color = input("Whats your color? ")
alien_color.lower()
if alien_color == "green":
    print("Congrats! You have just earned 5 points")
elif alien_color == "red":
    print("Oops! Too bad, you're a scammer.")
elif alien_color == "yellow":
    print("You have earned 3 points")
else:
    print("Your color is not among the options. Sorry!")
print("Thanks for playing!")

