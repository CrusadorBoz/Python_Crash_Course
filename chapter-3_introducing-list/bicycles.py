# [] indicate a list.  Individual elements are separated by commas
bicyles = ['trek', 'cannaondale', 'redline', 'specialized']
print(bicyles)

# To access elements in a list
print(bicyles[1])
print(bicyles[1].title())  # You can print in a more formal way.  Cap first letter
print(bicyles[-1])  # Use the -1 to return the last element in the list

# You can use individual items from a list in a sentence
message = f"My first bicycle was a {bicyles[1].title()}"

print(message)
