#!/usr/bin/python3.6
print("")

#lower case string will get the method title applied to it to make every first letter upper case
name = "evan rauner"
print(name.title())
print("------")

#upper case
print(name.upper())
print("------")

#lower case
#this use case is good for storing data
print(name.lower())
print("------")


#stripping whitespace
favorite_language = "python   "


#no strip
print(favorite_language)

#stripped right side of value
favorite_language.rstrip()
print(favorite_language)

#stripped left side of value
favorite_language.lstrip()
print(favorite_language)

#stripped both sides of value
favorite_language.strip()
print(favorite_language)

#to remove permananently throughout your script
#re-assign the variable to stripped value
favorite_language = favorite_language.rstrip()




print("------")




