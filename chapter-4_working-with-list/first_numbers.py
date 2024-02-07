# To show a series of numbers use the range() function
# Below only prints 1 through 4.  Another off-by-one behavior.
for value in range(1, 5):
    print(value)

print("------")
# To print actual 1 through 5
for value in range(1, 6):
    print(value)

# You can assign a range of numbers to a list
numbers = list(range(1, 6))
print(numbers)
