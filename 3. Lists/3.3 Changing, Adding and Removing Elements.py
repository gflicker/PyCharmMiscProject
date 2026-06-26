#Changing values in a list
names_of_friends = ["Rose", "Patricia", "Haggai", "Estina", "Nachi"]
print(names_of_friends)

#We want to remove the item at number 2
names_of_friends[1] = "Precious" #Changing only what is in the range
print(names_of_friends)

#Appending, adding to last in a list
names_of_friends.append("Sunwell") #This puts sunwell after Nachi, the last element
print(names_of_friends)

#Append used to add items to an empty list
mySisters = []
mySisters.append("Precious")
mySisters.append("Persida")
mySisters.append("Lilly Nana")
print(mySisters)

#Insert method, inserts at a named index and pushes the item at that index
mySisters.insert(1, "Metreny")
print(mySisters)

#del method to remove items from the list
del mySisters[1]
print(mySisters)

#Removing items using 'pop' method
popped_name = names_of_friends.pop()
print(names_of_friends)
print(popped_name)

#Popping items from any position in a list
popped_2_name = names_of_friends.pop(1)
print(f'The name that has been popped out is {popped_2_name}.')

#Removing an Item by Value
mySisters.remove("Persida")
print(mySisters)