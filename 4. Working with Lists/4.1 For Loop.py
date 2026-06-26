#Looping through a list using the for loop
myPeople = ["Rose", "Carol", "Sunwell", "Persida", "Precious"]
for name in myPeople:
    print(name)
print("Thank you.")

#Doing more now with the names using string functions
myPeople.sort(reverse=True)
NotMyPeople = myPeople.pop(4)
for name in myPeople:
    print(f'{name.upper()}, you are the best.')
print(f'{NotMyPeople} is not my relative but a friend.')