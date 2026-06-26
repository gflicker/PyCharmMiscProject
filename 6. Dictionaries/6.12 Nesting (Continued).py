#Storing a dictionaries in a list or list of items as values in a dictionary
#More robust nesting of dictionaries into a list
students = []
#while len(students) < 30: This while loop also works here
for student_numbers in range(5):#It will print 30 if no starting index
    new_student = {"Name": input("Student Name: "), "Subject": "Biology", "Grade":"A"}
    students.append(new_student) #Updating the list students
#Printing the first 5 students
for student in students[:5]:
    print(student)

#Checking to see how many students have been added to the list
print(f'Total number of students: {len(students)}')

#Changing names, subject and grade
for student in students[:5]:
    if student["Name"] == "Rose":
        student["Grade"] = "A"
        student["Subject"] = "Biology"
    elif student["Name"] == "Sunwell":
        student["Subject"] = "Computer Science"
        student["Grade"] = "B"
    elif student["Name"] == "Givious":
        student["Subject"] = "Maths"
        student["Grade"] = "A+"
    elif student["Name"] == "Haggai":
        student["Subject"] = "Maths"
        student["Grade"] = "A"
    elif student["Name"] == "Kelvin":
        student["Subject"] = "Commerce"
    elif student["Name"] == "William":
        student["Subject"] = "Accounts"
        student["Grade"] = "A"
    print(f"{student}")