#Letting the program run until a user ends it
# numberOfpuls = 0
# while numberOfpuls < 2:
#     numberOfpuls += 1
active = True
while active:
    print("\nHere are your results: ")
    grade = {
        "Student" : input("Student Name: "),
        "Class" : input("Class: "),
        "Term" : input("Term: "),
        "Mathematics": input("Mathematics: "),
        "Physics": input("Physics: "),
        "Chemistry": input("Chemistry: "),
        "Computer": input("Computer: "),

    }
# Student_ID = ""
# while Student_ID != "quit":
#     Student_ID = input("Enter Student ID: ")
    if grade["Student"] == "quit":
        active = False
    else:
        print("Here are your results:")
        for key, value in grade.items():
            print(f'{key}: {value}')

