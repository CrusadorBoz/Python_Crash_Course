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
jon_value = favorite_languages.get('john', 'There is not data for this key')
print(jon_value)

print("----------------------------------------------------")

# Looping through the dictionary
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
