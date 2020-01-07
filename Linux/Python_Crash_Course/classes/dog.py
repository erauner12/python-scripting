#!/usr/bin/python3.6

#/mnt/c/dev/python-scripting/Linux/Python_Crash_Course/classes


class Dog():

    def __init__(self, name, age):
        """Inititializing name and age attributes of dog"""
        self.name = name
        self.age = age


    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to command"""
        print(self.name.title() + " is now rolling over")



my_dog = Dog('Macy', 10)
your_dog = Dog('Winnie', 6)


# My Dog
print("This is my dog:")
print("Name: " + my_dog.name)
print("Age: " + str(my_dog.age))

my_dog.sit()
my_dog.roll_over()

print("\n")
# Your Dog

print("This is your dog:")
print("Name: " + your_dog.name)
print("Age: " + str(your_dog.age))

your_dog.sit()
your_dog.roll_over()
