#Making a function which tells what has to be printed
def printing_models(unprinted_models):
    while unprinted_models:
        printed_models = unprinted_models.pop()
        print(f'\t- {printed_models.title()}')