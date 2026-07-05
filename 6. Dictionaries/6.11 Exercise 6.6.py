#Looping through pupils who wrote the test and those who have to retake
favorite_subject = {
    "Givious": "Mathematics",
    "Rose": "Biology",
    "Sunwell": "Computer Science",
    "Haggai": "Mathematics",
    "Kelvin": "Accounts",
    "Precious": "Agriculture",
    "Carol": "Agriculture",
    "Voster": "Mathematics",
    "Ivorr": "Art",
    "Derick": "Physics",
}
retaking_the_poll = [
    "Estina", "Nachili", "Lizzy", "Patricia", "Steven", "Martin",
    "Givious", "Ivorr", "Rose"
]
sorted(retaking_the_poll)
sorted(favorite_subject.keys())
for pupil in favorite_subject.keys():
    print(f'\t{pupil}')
    if pupil in retaking_the_poll:
        print(f'\t\tHello {pupil}, your favourite subject is {favorite_subject[pupil]}')
    else:
        print(f'\t\t{pupil} please tell us your favourite subject')
#Listing number of subjects and removing duplicates
print("\nHere is a list of subjects that were surveyed:")
for subject in set(favorite_subject.values()):
    print(f'\t{subject.upper()}')