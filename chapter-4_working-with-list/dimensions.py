dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# You cannot change the tuple.  ex: dimensions[0] = 250
# tuples have to have a comma even for one element.
my_t = (3,)
print(my_t)

# You loop through a tuple the same as a list
for dimension in dimensions:
    print(dimension)

# Writing over a tuple
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions")
for dimension in dimensions:
    print(dimension)
