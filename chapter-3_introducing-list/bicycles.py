# [] indicate a list.  Individual elements are separated by commas
bicycles = ['trek', 'cannondale', 'redline', 'diamondback', 'specialized']
print(bicycles)

# To access elements in a list
print(bicycles[1])
print(bicycles[3].title())  # You can print in a more formal way.  Cap first letter
print(bicycles[-1])  # Use the -1 to return the last element in the list

# You can use individual items from a list in a sentence
message = f"My first bicycle was a {bicycles[1].title()}"

print(message)
