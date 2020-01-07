#!/usr/bin/python3.6
print("")

#/mnt/c/dev/python-scripting/Linux/Python_Crash_Course/functions

# shirt_size defaults to large if the user does not provide a size
def make_shirt(text_on_shirt,shirt_size='Large'):
    """ Taking info from user to put on shirt """
    print("Here is what shirt you picked: ")
    print("Shirt Size: " + shirt_size)
    print("Custom Text: " + text_on_shirt)


# notice how we did not provide a parameter here and it the output shows large
make_shirt('Yo')
print("----")
make_shirt('small','where dey at doe')
