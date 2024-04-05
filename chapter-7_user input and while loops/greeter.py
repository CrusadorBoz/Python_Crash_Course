name = input("Please enter your name: ")
print(f"Hello, {name}")

print("-------------------------------------------")

prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"Hello, {name}")

print("-------------------------------------------")

age = input("How old are you? ")
print(age)
print(f"You are, {age}")

# You cannot compare string to numerical like below without converting.
# You have to convert it to int
age = int(age)
if age >= 21:
    print(f"{age} Is older than 21!")
else:
    print(f"{age} is not older than 21!")
