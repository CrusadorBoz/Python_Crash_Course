# Slicing a list - working with certain number of elements in a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(len(players))
print(players[0:3])

# To print the first four elements
print(players[:4])

# You can also print from a certain element to the end
print(players[2:])

# Print the last three players.
print(players[-3:])

# Looping through a slice
print("Here are the fierst three players on my team:")
for player in players[:3]:
    print(player.title())
