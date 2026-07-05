#Passing a list as a parameter into a function
#Copying elements from one list to another
def send_messages(unsent_messages, sent_messages):
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f'The current message: {current_message}')
        sent_messages.append(current_message)

def show_sent_messages(sent_messages):
    print(f'The following messages have been sent:')
    for sent_message in sent_messages:
        print(sent_message)

unsent_messages = ["Sunwell", "Haggai", "Kelvin", "Precious", "Persida", "Tristan","Lizzy"]
sent_messages = []

#calling functions
send_messages(unsent_messages, sent_messages)
show_sent_messages(sent_messages)

