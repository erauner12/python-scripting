motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)
print("----")

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
print("----")


# inserting in first index
braapbraap = "crotch rocket"
motorcycles.insert(0,braapbraap)
print(motorcycles)

print(f"\nI could buy a {braapbraap}")


print("nvm, I do not want the {braapbraap}")
print(motorcycles)
print("----")

# remove the first index
del motorcycles[0]

print(motorcycles)

print("----")
# -1 is the last element in the list
print(f"getting rid the last back I got: {motorcycles[-1]}")

# use pop method to get rid of the last item in the list

popped_motorcycle = motorcycles.pop()

print(motorcycles)
print(f"removed {popped_motorcycle}")
print("----")


# you can pop anything in the list and recall it afer it is gone

print(f"Gotta get rid of the first bike I got {motorcycles[0]}")

print(motorcycles)

first_owned = motorcycles.pop(0)

print(f"Well I got rid of {first_owned.title()}")

print(motorcycles)

print("----")

# you can call out which item(s) you want to remove
print("Going to remove my last bike")

print(motorcycles)
motorcycles.remove('yamaha')

print(motorcycles)





