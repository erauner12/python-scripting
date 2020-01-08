#!/usr/bin/python3.6

#/mnt/c/dev/python-scripting/Linux/Python_Crash_Course/classes


class Car():
    """ A simple attempt to represet a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odomoter_reading = 0

    def get_descriptive_name(self):
        """Retrun a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print("The Car has " + str(self.odomoter_reading) + " miles on it")


    def update_odometer(self, mileage):
        """update the odometer on an instance of a car"""
        self.odomoter_reading = mileage

    def increment_odometer(self,miles):
        """Add the given amount to the odometer reading"""
        self.odomoter_reading += miles





my_new_car = Car(make='Audi',model='a4', year=2016)

# get all attributes of the car via the function defined in the Car class
print(my_new_car.get_descriptive_name())
print("--------")

# Pass no miles

my_new_car.read_odometer()
print("--------")

# You can change the value through an instance, through a method, or increment the value through the method:

# directly
my_new_car.odomoter_reading = 60000
my_new_car.read_odometer()
print("--------")


# through a method, passing an argument of 80000 into the function above

my_new_car.update_odometer(80000)
my_new_car.read_odometer()
print("--------")


my_used_car = Car("Ford","Ranger","1993")
print(my_used_car.get_descriptive_name())

# calling function to increment the odometer reading
my_used_car.increment_odometer(20000)
my_used_car.read_odometer()
print("--------")

# Doubles the odometer reading by incrementing it
my_used_car.increment_odometer(20000)
my_used_car.read_odometer()
print("--------")




print("--------")
print("--------")
print("--------")









   