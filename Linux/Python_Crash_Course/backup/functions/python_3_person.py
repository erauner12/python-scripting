#!/usr/bin/python3.6
print("")

# This function needs a first and last name, but age is optional
def build_person(first_name,last_name,age=''):
    """Returns a dictionary about a person"""
    person = {'first': first_name,'last': last_name}
    if age:
        person['age'] = age
    return person

# no age provided
rockstar = build_person(first_name='jimi',last_name='hendrix')
print(rockstar)
print("----")

# Age provided
rockstar = build_person(first_name='jimi',last_name='hendrix',age='50')

print(rockstar)






