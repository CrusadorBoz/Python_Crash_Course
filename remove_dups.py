# from @bOO1 YouTube

old = ['a', 'b', 'a', 'c', 'b', 'a']

# most common way - sets do not keep order
noorder = list(set(old))  # Does not maintain order

new = []  # create a new list to keep order. This works... 

for item in old:
    if item not in new:
        new.append(item)
    
# You can use a dictionary to remove dups - improved way
best_dictionary = dict.fromkeys(old)  # This creates a dictionary...they cannot have dups
best = list(dict.fromkeys(old))

print(noorder)
print(new)
print(best)
