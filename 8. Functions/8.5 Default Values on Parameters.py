"""Some Parameters can be set as default and skip some arguments when calling a function"""
student_name = input('Student Name: ')
def students(student_name, Class='G12'):
    print(f'Student Name: {student_name.title()}\nClass: {Class}')
#Here there's only one argument but the output will also put the default value 'Class'
students(student_name)

