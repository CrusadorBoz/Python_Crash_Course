# Copying list
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# Note: you have to use slice.  friends_foods = my_foods does not work.
# Slicing is the [:], enables selection of certain elements.

### friend_foods = my_foods ###  DOES NOT WORK, try it.

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are: ")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
