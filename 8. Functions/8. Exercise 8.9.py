#Passing a list as a parameter into a function
def show_messages(siblings):
    print("Here are my siblings:")
    for sibling in siblings:
        print(f'\t{sibling}')
#a list were to draw my siblings
mySiblings = ["Sunwell", "Haggai", "Kelvin", "Precious", "Persida", "Tristan","Lizzy"]
#Calling the function
show_messages(mySiblings)