# Create a motorcycle list
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# show one element from the motorcycles list
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding items to the list
motorcycles.append('ducati')
print(motorcycles)

# You can create a blank list and add later
motorcycle_companies = []
motorcycle_companies.append('honda')
motorcycle_companies.append('kawasaki')
motorcycle_companies.append('susuki')
print(motorcycle_companies)

# You can insert at any postion
motorcycle_companies.insert(2, 'yamaha')
print(motorcycle_companies)

# You can delete a element at a position
del motorcycle_companies[2]

print(motorcycle_companies)

# You can use pop() to remove the last element in the list.  
popped_MoCompanies = motorcycle_companies.pop()
print(motorcycle_companies)
print(popped_MoCompanies)

# We can use the pop to print a sequece like if the motorcycles where in the order you owned them
first_owned = motorcycles.pop(0)
print(f"This first brand of motorcyle I owned was a {first_owned.title()}.")
