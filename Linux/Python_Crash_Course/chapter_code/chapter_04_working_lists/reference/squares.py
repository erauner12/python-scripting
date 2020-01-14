

# ** means to the power of
# so this function will multiply every number between one and ten by the power of 2 and assign that value to every the next item in the list
squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)


# using list comprehension, we can insert the values of the expression "value**2" directly into the list squares
squares2 = [value**2 for value in range(1, 11)]
print(squares2)


