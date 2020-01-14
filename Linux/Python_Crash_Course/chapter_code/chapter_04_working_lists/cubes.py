cubes = []

for value in range(1,11):
    cubes.append(value**3)

for cube in cubes:
    print(cube)


print("-----")


cubes2 = [value**3 for value in range(1,11)]
print(cubes2)
