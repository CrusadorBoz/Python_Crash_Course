alien_0 = {'color': 'green', 'points': 5}

# print(alien_0['color'])
# print(alien_0['points'])
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
print(alien_0)

new_points = alien_0['points']
# print(f"You just earned {new_points} points!")

# Adding new key-value pairs
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# You can start with an empty dictionary and add to it later.
print("-------------------------------------")

alien_1 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original x-position: {alien_1['x_position']}")
alien_1['speed'] = 'fast'

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_1['speed'] == 'slow':
    x_increment = 1
elif alien_1['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_1['x_position'] = alien_1['x_position'] + x_increment

print(f"New x-position: {alien_1['x_position']}")
print("-------------------------------------")

# Removing key value pairs
alien_2 = {'color': 'green', 'points': 5}
print(alien_2)

del alien_2['points']
print(alien_2)
