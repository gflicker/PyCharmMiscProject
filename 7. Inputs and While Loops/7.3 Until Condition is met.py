#Letting the user choose when to quit
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'q' to quit. "

message = ""
while message != "q":
    message = input(prompt)
    print(message)