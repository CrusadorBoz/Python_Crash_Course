alien_0 = {'color': 'green', 'points': 6}
print(alien_0['color'])

# to add new key values
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# To delete a key value
del alien_0['points']
print(alien_0)

# Modifying values
house_0 = {'bedrooms': 'four', 'bathrooms': 1, 'square_feet': 1456}
print(f"This house has {house_0['bedrooms']} bedrooms")
# Use if statements to have comments on house values
if house_0['bathrooms'] == 3:
    print("This house has 3 bathrooms, AWESOME!")
elif house_0['bathrooms'] <= 2:
    print("This house is not good.  Not enough shitters")
else:
    print("Stay away, this house has to many shitters")
