#Giving python options of what to do when an error is expected
try:
    print(5/0)
except ZeroDivisionError:
    print('You cannot divide by zero')