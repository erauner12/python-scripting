#!/usr/bin/python3.6
print("")

#/mnt/c/dev/python-scripting/Linux/Python_Crash_Course/functions

# Functions are most often they are just doing something to the paraemeters and passing it back
# This is what return is for
def get_formatted_name(first_name,last_name,middle_name =''):
    """Return a neatly formatted name to the user"""
    #if a middle name is passed, then if will be equal to true which will return all three parameters
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    #if there was no middle name passed into the function, full_name will only have the first and last name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title() 

# We are passing lower case names as arguments and then recieving a value in return which is getting passed into the variable
rockstar1 = get_formatted_name('jimi','hendrix')

print(rockstar1)
print("----")
# adding a middle name argument which is optional
rockstar2 = get_formatted_name(first_name='jimi', middle_name='fake',last_name='hendrix')
print(rockstar2)



