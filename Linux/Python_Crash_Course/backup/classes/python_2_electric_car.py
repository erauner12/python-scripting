#!/usr/bin/python3.6

#/mnt/c/dev/python-scripting/Linux/Python_Crash_Course/classes



class Car():
    """ A simple attempt to represet a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odomoter_reading = 0
        self.fuel = 0

    def get_make(self):
        """Get just the make of the car"""
        car_make = self.make
        return car_make.title()

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

    def display_fuel_gauge(self):
        print("This car has " + str(self.fuel) + " gallons of gas left")

    def fill_gas_tank(self,gas):
        self.fuel += gas

# We do not want to crowd up electric car with all the details of it's battery so we can make a new instance of it that does not inherit from Car or ElectricCar
class Battery():
    """A simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=70):
        self.battery_size = battery_size


    def describe_battery(self):
        """Print a statement that describes the size of the battery"""
        print("This car has " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles"""
    
    def __init__(self, make, model, year):
        """Initiatialize attributes of a parent class"""
        # this will initialize the properties we set up in Car. The commonalities that all cars have
        super().__init__(make, model, year)
        self.battery = Battery()
    
    # Electric cars do not have gas so we must override one of the base characteristics of Car

    def fill_gas_tank(self, gas):
        """Electric cars do not have gas tanks"""
        print("this car does not have a gas tank")
        






my_tesla = ElectricCar("Tesla", "Model S", 2018)
print(my_tesla.get_descriptive_name())

# Print just the make
print(my_tesla.get_make())

print("----------")

# Call method that describes how much battery the car has
my_tesla.battery.describe_battery()
print("----------")


print("----------")
# Created a whole new set of methods regarding fuel
my_car = Car("Gas","Guzzer","1805")

my_car.fill_gas_tank(30)
my_car.display_fuel_gauge()
print("----------")


# Now let's test our override
print(my_tesla.fill_gas_tank(80))
print("----------")

# Call method that describe both properties now available after adding the Battery class
print(my_tesla.get_descriptive_name())
print(my_tesla.battery.describe_battery())


print("----------")


