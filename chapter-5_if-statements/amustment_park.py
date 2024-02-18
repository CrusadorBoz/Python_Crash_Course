age = 19
if age < 4:
    price = 0
    # Redundant
    # print("Your admission cost is $0")
elif age < 18:
    price = 25
    # Redundant
    # print("Your admission cost is $25")
else:
    price = 40
    # Redundant
    # print("Your admission cost is $40")

print(f"Your admission cost is ${price}")
