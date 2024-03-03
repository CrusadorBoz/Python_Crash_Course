favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# You can look up a certain person to see what language they like
language = favorite_languages['sarah'].title()
print(f"Sarah's Favorite language is {language}.")
print(favorite_languages['sarah'])

# To use the get() function to access values
# we will use John to show that we can return a message if not there
jon_value = favorite_languages.get('john', 'There is no data for this key')
print(jon_value)

print("----------------------------------------------------")

# Looping through the dictionary
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("----------------------------------------------------")

for name in favorite_languages.keys():
    print(name.title())

print("----------------------------------------------------")

for value in favorite_languages.values():
    print(value.title())

print("----------------------------------------------------")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi, {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}")


if 'erin' not in favorite_languages.keys():
    print(f"Erin, please take our pool")

print("----------------------------------------------------")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

print("----------------------------------------------------")

print(f"The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("----------------------------------------------------")

print(f"The following languages have been mentioned:")
for language in set(favorite_languages.values()):   # The set gets a colleciton that is unique.  No duplicates
    print(language.title())

print("----------------------------------------------------")

languages = {'python', 'rust', 'python', 'c'}  # This is a set.  Does not allow duplicates.  Looks like a Dictionary
print(languages)
