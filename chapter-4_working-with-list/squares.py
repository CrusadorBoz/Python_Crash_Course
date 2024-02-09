# List Comprehensions: You can combine into one line a for loop and appending the list
squares = [value ** 2 for value in range(1, 11)]
# You use a desc name for var.  then the expression. then for loop  No colon!
# It takes practice to write list comprehensions.  Very efficient once you learn.
# Try to do them when you are typing multiple lines.
print(squares)

### Exercise 1 ### 
# Write a program to create a list of 1,000,000 numbers.  The print
million = [value + 1 for value in range(1, 10000000)]
print(sum(million))
print(million)
