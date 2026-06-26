#Adding text to an already existing file, by opening a file in append mode
file_name = 'programming.txt'

with open(file_name, 'a') as update_object:
    update_object.write('Python is becoming my favorite language.\n')
    update_object.write('I want to stay focused and disciplined to achieve more.\n')
#This here updates shows the updated file, lets try to read it now
print('SEE HOW THE FILE HAS BEEN UPDATED')
filename = 'programming.txt'
with open(filename) as update_script:
    view_update = update_script.read()
print(view_update)