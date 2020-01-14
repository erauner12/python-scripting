dimensions = (200, 50)
print("Original Dimensions")
for dimension in dimensions:
    print(dimension)


print("---")

print(dimensions[0])
print(dimensions[1])


# define a tuple with one element

my_tuple = (3,)

# you cannot modify a tuple but you can assign a new value to a variable that represents a tuple
dimensions = (400,100)
print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)