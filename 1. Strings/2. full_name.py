first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
#Composing a message using f-strings
print(f"Hello, {full_name.title()}")

#Assigning it to a variable
message = f"\tHello, {full_name.title()}"
print(message)
#For indenting we use the "\t" and for new line "\n".