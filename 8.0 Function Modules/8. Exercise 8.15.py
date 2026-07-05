# #Making a function which tells what has to be printed
# def printing_models(unprinted_models):
#     while unprinted_models:
#         printed_models = unprinted_models.pop()
#         print(f'\t- {printed_models}')
from exercise_modules import printing_functions

"""Here is the list of T-Shirts to be printed"""
shirts = ["golf", "corporate", "polo", "long sleeves", "dress shirts"]
printing_functions.printing_models(shirts)