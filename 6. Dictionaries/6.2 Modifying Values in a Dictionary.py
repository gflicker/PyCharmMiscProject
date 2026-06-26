#Changing values in a dictionary
alien_0 = {'color': 'green'}
print(f'The alien is {alien_0["color"]}')
#Changing color by assigning it another color
alien_0['color'] = 'yellow'
print(f'The alien is now {alien_0["color"]}')

#More complex example on changing values in a dictionary
alien_1 = {
    'x_position': 0, 'y_position': 25, 'speed': input('Enter speed: ')
    }
print(f'Original position: {alien_1["x_position"]}')
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    #This is fast
    x_increment = 3
#New position is the original plus the increment.
alien_1['x_position'] = alien_1['x_position'] + x_increment

#The new position now
print(f'New position: {alien_1["x_position"]}')
