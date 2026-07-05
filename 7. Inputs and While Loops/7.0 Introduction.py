#If I want more than one line to appear under the input function
prompt = ("If you tell us who you are, we can "
          "personalize the messages you see")
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f'\nHello, {name}!')