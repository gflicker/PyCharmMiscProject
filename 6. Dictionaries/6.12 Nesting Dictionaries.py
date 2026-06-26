#Storing a dictionaries in a list or list of items as values in a dictionary
#Below are three dictionaries for three students
student1 = {"Name": "Rose", "subject": "Biology", "Grade":"A"}
student2 = {"Name": "Givious", "subject": "Maths", "Grade":"A"}
student3 = {"Name": "Sunwell", "subject": "Computer Science", "Grade":"A"}

#Here we put dictionaries in a list
students = [student1, student2, student3]
#Looping three items in a list, meaning three dictionaries
for student in students:
    print(student)

#Making a more robust list
