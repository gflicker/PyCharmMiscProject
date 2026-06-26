#Looping through a dictionary
users = {
    "username": "caramel",
    "first_name": "Rose",
    "last_name": "Zulu",
    "status": "Engaged"
}
#To access everything at once, we loop
for key, value in users.items():
    print(f'{key.title()}: {value.title()}')

#A loop without using the words "key" and "value
print("\nHere are my friend's programming languages:")
programming_languages = {
    "Sunwell": "Python",
    "Caramel": "JavaScript",
    "Haggai": "JavaScript",
    "Precious": "PHP",
    "Estina": "C#",
    "Givious": "C++",
}
for name, language in programming_languages.items():
    print(f"{name.title()}'s favorite programming language is {language}")

#When you just want to loop through a few values not all values
print("\nHere are my friend's names:")
for name in programming_languages.keys():
    print(name) #Printing only the keys only, that is names of people

#Printing values only
print("\nHere is the list of Programming Languages that are common:")
for language in programming_languages.values():
    print(language)

#Writing a message to the selected few in a looped Dictionary
print("\nCustomized message only to a few elites:")
friends = ["Givious", "Caramel"]
for name in programming_languages.keys():
    print(name)

    if name in friends:
        language = programming_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")