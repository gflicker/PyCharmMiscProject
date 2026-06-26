#Passing a lot of parameters as a user wishes
def cambridge_subjects(*subjects):
    """Printing a list of subjecst under Cambridge Primary Curriculum"""
    #print(subjects)
    print("Here are some subjects under the Cambridge Primary Curriculum:")
    for subject in subjects:
        print(f' - {subject}')
#Calling a function
cambridge_subjects("Computing")
#Calling a function with more arguments
cambridge_subjects("Global Perspective", "Foreign Language",
                   "Mathematics", "Science", "Dital Literacy", "English")