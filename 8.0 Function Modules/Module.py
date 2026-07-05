#Making a module and importing it
def student(name, *subjects):
    """A summary of the student's information"""
    print(f'Your name is {name} and here are your subjects: ')
    for subject in subjects:
        print(f' - {subject}')