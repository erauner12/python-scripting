people = {
    'person_1': {
        'first_name':'Erik',
        'last_name':'Stidsen',
        'age':28,
        'city':'OP'
    },
    'person_2': {
        'first_name':'Evan',
        'last_name':'Rauner',
        'age':26,
        'city':'Mission'
    }
    }


#This is how you print out the values
for names, properties in people.items():
    print(f"\nName: {names}")
    print(f"About:")
    full_name = f"{properties['first_name']} {properties['last_name']}"
    print(f"\tFull Name: {full_name}")
    print(f"\tAge: {properties['age']}")
    print(f"\tCity: {properties['city']}")


