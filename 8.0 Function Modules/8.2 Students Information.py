#We're now importing the functions which helps us to see student's information
import Module
#Calling the function
Module.student("givious","Maths", "Physics", "Python", "Computing")

#Importing only one function not the entire moduble
from Module import student
student("Sunwell", "Physics", "Python", "Computing")

#Importing a function and giving it an alias name
import Module as module
module.student("Haggai", "Maths", "Commerce", "English")

#Importing all functions in a module
from Module import *
module.student("Kelvin", "Maths", "Accounts", "Commerce")