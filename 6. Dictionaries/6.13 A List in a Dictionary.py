#Store information about a certain Pizza being ordered
pizza = {
    "crust": "thick",
    "topping": ["mushrooms", "extra cheese", "extra chicken"]
}
#Summarize the order
print(f'You ordered {pizza["crust"]}-crust pizza '
      f'with the following topping:')
for topping in pizza["topping"]:
    print("\t" + topping.title())

#A list inside a dictionary of favorite programming languages.
favorite_subjects = {
    "\nprecious": ["Agriculture"],
    "givious": ["Mathematics","Physics","Coding"],
    "rose": ["Biology", "Food and Nutrition"],
    "sunwell": ["Computer Science"],
}#To loop successfully make sure all the values are enclosed as a list
for name, subjects in favorite_subjects.items():
    if len(subjects) == 1:
        print(f"{name.title()}'s favorite language is:")
    else:
        print(f"{name.title()}'s favorite languages are:")
    for subject in subjects:
        print(f"\t{subject.title()}")