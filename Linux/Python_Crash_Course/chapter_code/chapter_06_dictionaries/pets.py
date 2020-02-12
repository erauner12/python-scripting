
pets = []

pet1 = {
    'Erik':'dog'
}

pet2 = {
    'Evan':'cat'
}

pets.append(pet1)
pets.append(pet2)


for pet in pets:
    for owner_name,pet_name in pet.items():
        print(f"{owner_name} is the owner of a {pet_name}")