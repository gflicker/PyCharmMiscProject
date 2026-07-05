#Creating a file by writing one using python.
filename = 'rose.txt'
with open(r'E:\Studio 1\Videos\Python\Crash Course\10. Files and Exceptions\rose.txt', 'w') as file_object:
    file_object.write("Hello Rose, I love you so much.")

#Opening the file we have just created
with open('rose.txt') as pro:
    prog = pro.read()
print(prog)

