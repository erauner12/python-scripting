
river = {
    'nile':'egypt',
    'amazon':'Columbia',
    'rio':'gulf of mexio'
}

print("---------")

# both
for key,value in river.items():
    print(f"The {key} runs through the {value}")

print("---------")


# just keys
for key in river.keys():
    print(f"{key}")


print("---------")

# just values
for value in river.values():
    print(f"{value}")
