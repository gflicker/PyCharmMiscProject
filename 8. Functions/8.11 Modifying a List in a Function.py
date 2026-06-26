#This is modifying a list without a function
#About printing shirts
unprinted_designs = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []

#Moving each design to completed models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f'Printing model: {current_design.title()}')
    completed_models.append(current_design.title())

#Showing all completed models
print(f'\nThe following models have been printed: ')
for completed_model in completed_models:
    print(completed_model)