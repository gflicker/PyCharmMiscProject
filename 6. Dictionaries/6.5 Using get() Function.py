#using the get() function to access values
subject = {
    'Mathematics': int(input("Mathematics: ")),
    'Science': int(input("Science: ")),
    'Computer Studies': int(input("Computer Studies: ")),
    }
# "print(subject ['points'])" The key does not exist, therefore KeyError
#Get function helps us display a message if a key does not exist
subject_value = subject.get('Points', 'No subject Points')
print(subject_value)

#If the key value is there, the value will be retrieved
Mathematics = subject.get('Mathematics', 'No Mathematics')
print(Mathematics)

