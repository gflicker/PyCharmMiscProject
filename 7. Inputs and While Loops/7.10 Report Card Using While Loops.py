#Creating a report card to capture student's scores
StudentReportCard = {}
report_card = True
while report_card:
    StudentName = input("Enter the Student's Name: ")
    Name = "Name"

    Mathematics = "Mathematics"
    Maths = input("Mathematics: ")

    Physics = "Physics"
    Phy = input("Physics: ")

    Biology = "Biology"
    Bios = input("Biology: ")

    Computer = "Computer"
    Comp = input("Computer: ")

    #Adding them to the dictionary
    StudentReportCard[Name] = StudentName
    StudentReportCard[Mathematics] = Maths
    StudentReportCard[Physics] = Phy
    StudentReportCard[Biology] = Bios
    StudentReportCard[Computer] = Comp

    #Choosing to continue or to end
    Proceed = input("Would you like to continue (y/n): ")
    if Proceed == 'n':
        report_card = False
    #Writing the scores which have been captured
    print(f'\n-----------The Results for {StudentName}----------')
    for key, value in StudentReportCard.items():
        print(f'{key}: {value}')
