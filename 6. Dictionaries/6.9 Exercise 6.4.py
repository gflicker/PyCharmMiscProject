#Looping through a dictionary
Grossary = {
    "Python": "This is a programming langauge which is widely used.",
    "Data Type": "Lists, Numbers, boolean, tuples, dictionaries, function",
    "Dictionary": "Data type which stores key-value pairs of information",
    "List Comprehension": "Putting code inside a list, "
                          "no need to write it outside the list",
    "Slicing":"Used to get just needed information in a list"
}


#Adding more key-value pairs to the dictionary
Grossary["Loop"] = ("In programming this means keeping on executing the code \n"
                    "\tuntil the stop condition is met.")
Grossary["Indenting"] = ("This is a style used to group codes together"
                         "\n\tfor style or linking code according to the way"
                         "they are related.")
Grossary["Dictionary and Set"] = ("The difference between the two is the way \n"
                                  "\tthey are written.\n"
                                  "\tA set is a list but enclosed with curly braces while\n"
                                  "\ta dictionary items are stored as pairs of keys and values\n"
                                  "\tseparated by a full colon.")
for term, defination in Grossary.items():
    print(f'{term}: {defination}')