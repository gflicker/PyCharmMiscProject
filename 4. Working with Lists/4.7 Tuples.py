#Creating tuples, permanent lists in other terms
#Dimensions of a rectangle
dimensions = (200,50)
#Accessing individual items, same as in lists
print(f'The length of this rectangle is {dimensions[0]}\n'
      f'and the width of this rectangle is {dimensions[1]}\n'
      f'Therefore, the area of this rectangle is {dimensions[0] * dimensions[1]}')
#We can't change an item in a tuple, here is an example
    #dimensions[0] = 250 This will produce an error.
    #print(f'The length of this rectangle is {dimensions[0]}\n')
