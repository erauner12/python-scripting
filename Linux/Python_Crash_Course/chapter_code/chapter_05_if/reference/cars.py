cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# a statement. the value of care is equal to 'audi'
car = 'audi'

# a condition. Is the value of equal to 'bmw'
car == 'BMW'

print("---")


# testing for equality is always case sensiitive.
# these are not equal
car = 'Audi'

car == 'audi'

# now they are equal
car.lower() == 'audi'




