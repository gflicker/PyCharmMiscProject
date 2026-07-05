my_Siblings = ["Sunwell", "Haggai", "Kelvin", "Precious", "Persida", "Tristan"]
print("Here is the original list:")
print(my_Siblings)

#Sorted list in alphabetical order
print("\nHere is the sorted list:")
print(sorted(my_Siblings))
print("\nHere is the original list, still intact, temporarily sorted:")
print(my_Siblings)

#Printing a list in reverse order
my_Siblings.reverse()
print(my_Siblings)

#Negating the reverse on top
my_Siblings.reverse() #reversing what was reversing, more like undoing
print(my_Siblings)
