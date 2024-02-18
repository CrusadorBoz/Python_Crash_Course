requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# We cannot use elif on this one because it would break out and not work.
if 'mushrooms' in requested_toppings:
    print("Adding Mushrooms.")
if 'pepperoni' in requested_toppings:
    print('Adding Pepperoni.')
if 'extra cheese' in requested_toppings:
    print('Adding Extra Cheese.')

print(f"\n*** We have finished making your pizza ***\n\n")


# printing all the requested items. Checking for special items
for requested_toppings in requested_toppings:
    if requested_toppings == 'green peppers':
        print("Sorry we are out of green peppers right now")
    else:
        print(f"Adding {requested_toppings}")

print(f"\n*** We have finished making your pizza ***\n")


# Checking if list is empty
toppings_requested = []

if toppings_requested:
    for toppings_request in toppings_requested:
        print(f"Adding {toppings_requested}.")
    print(f"\nWe have finished making your pizza")
else:
    print("*** Are you sure you want a plain pizza ***")
