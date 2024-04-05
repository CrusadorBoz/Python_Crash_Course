# The Moddulo Operator can tell you if the integer is even or odd.

number = input("Enter a month, and I will tell you if it is even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even")
else:
    print(f"\nThe number {number} is odd")
