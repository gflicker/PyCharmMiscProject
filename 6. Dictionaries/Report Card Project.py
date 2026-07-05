#This is a small project for a school report card for students
report_card = {
    'Title': 'STUDENT REPORT CARD', 'School': 'G&R ACADAMY',
    'Name': input("Student Name: "), 'Year': int(input("Year: ")), 'Class': input("Class: "),
    'Term': int(input("Term: ")),
    }
subject = {
    'English': int(input("English: ")), 'Mathematics': int(input("Mathematics: ")),
    'Science': int(input("Science: ")), 'Biology': int(input("Biology: ")),
    'Music': int(input("Music: ")), 'Computer Studies': int(input("Computer Studies: ")),
    }
comment = subject

#English grading
if subject['English'] > 74:
    subject['English'] = 'A'
elif subject['English'] >= 65:
    subject['English'] = 'B'
elif subject['English'] >= 55:
    subject['English'] = 'C'
elif subject['English'] >= 40:
    subject['English'] = 'D'
else:
    subject['English'] = 'F'

#Mathematics grading
if subject['Mathematics'] > 74:
    subject['Mathematics'] = 'A'
elif subject['Mathematics'] >= 65:
    subject['Mathematics'] = 'B'
elif subject['Mathematics'] >= 55:
    subject['Mathematics'] = 'C'
elif subject['Mathematics'] >= 40:
    subject['Mathematics'] = 'D'
else:
    subject['Mathematics'] = 'F'
#Science grading
if subject['Science'] > 74:
    subject['Science'] = 'A'
elif subject['Science'] >= 65:
    subject['Science'] = 'B'
elif subject['Science'] >= 55:
    subject['Science'] = 'C'
elif subject['Science'] >= 40:
    subject['Science'] = 'D'
else:
    subject['Science'] = 'F'

#Biology grading
if subject['Biology'] > 74:
    subject['Biology'] = 'A'
elif subject['Biology'] >= 65:
    subject['Biology'] = 'B'
elif subject['Biology'] >= 55:
    subject['Biology'] = 'C'
elif subject['Biology'] >= 40:
    subject['Biology'] = 'D'
else:
    subject['Biology'] = 'F'

#Music grading
if subject['Music'] > 74:
    subject['Music'] = 'A'
elif subject['Music'] >= 65:
    subject['Music'] = 'B'
elif subject['Music'] >= 55:
    subject['Music'] = 'C'
elif subject['Music'] >= 40:
    subject['Music'] = 'D'
else:
    subject['Music'] = 'F'
#Computer Studies grading
if subject['Computer Studies'] > 74:
    subject['Computer Studies'] = 'A'
elif subject['Computer Studies'] >= 65:
    subject['Computer Studies'] = 'B'
elif subject['Computer Studies'] >= 55:
    subject['Computer Studies'] = 'C'
elif subject['Computer Studies'] >= 40:
    subject['Computer Studies'] = 'D'
else:
    subject['Computer Studies'] = 'F'
#Grading scale


#Main Body of the Report Card
print("################################################################|")
#Personal Details
print(f'|                         {report_card["School"]}                           |')
print(f'|                     {report_card["Title"]}                       |')

print(f'|  Name: {report_card["Name"]}                 Year: {report_card["Year"]}                     |')
print(f'|  Class: {report_card["Class"]}                    Term: {report_card["Term"]}                        |')
print(" ---------------------------------------------------------------")
#Subject, Grades and Feedback
print("|  SUBJECT                 |  GRADE  |                 COMMENT  |")
#for subject, grade in subject.items():
   # print(f'{subject} {grade}')
print(f'|  English                 |    {subject["English"]}    |                          |')
print(f'|  Mathematics             |    {subject["Mathematics"]}    |                          |')
print(f'|  Science                 |    {subject["Science"]}    |                          |')
print(f'|  Biology                 |    {subject["Biology"]}    |                          |')
print(f'|  Music                   |    {subject["Music"]}    |                          |')
print(f'|  Computer Studies        |    {subject["Computer Studies"]}    |                          |')
print("|###############################################################|")