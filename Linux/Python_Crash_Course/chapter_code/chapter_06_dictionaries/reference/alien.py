

alien_123 = {'color': 'red',
            'points':10}

print(alien_123['color'])
print(alien_123['points'])

print("---")

alien_345 = {'color': 'yellow',
            'points':15}

new_points = alien_345['points']
print(f"you just earned {new_points} points!")
del alien_345['points']
#remove the points key value pair
print(alien_345)



print("---")
alien_0 = {'color':'green','points':5}

alien_0 = {'color':'yellow'}
print(f"alien_0 is now {alien_0['color']}")

#you can list each property of a dictionary seperately
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'

print(f"Original position: {alien_0['x_position']}")


# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")






