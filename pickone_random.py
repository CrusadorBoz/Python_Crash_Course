import random

my_list = ["apple", "banana", "orange", "grape"]

# Pick one random item from the list and ensure it's unique
picked_item = random.sample(my_list, 1)[0]

print(f"Picked item: {picked_item}")
