### Sorting a list ###
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()  ## Sort changes the list forever.  Alphabetical
print(cars)

cars.sort(reverse=True)  ## reverse sort also changes permanently 
print(cars)

### To temporarily sort a list ###
cars_two = ['bmw', 'audi', 'toyota', 'subaru']

print("\nHere is the original list:")
print(cars_two)

print("\nHere is the sorted list:")
print(sorted(cars_two))

print("\nHere is the original list, again")
print(cars_two)

### Reverse order ### 
### This also is a permanent change ###
print("\nHere is the list reversed using the reverse method -- it is permanent")
cars_two.reverse()
print(cars_two)

### Finding a length of a list ###
print(len(cars_two))
