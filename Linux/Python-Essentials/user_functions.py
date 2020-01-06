#!/usr/bin/python3.6



def authenticate(username,password):
    for u in username:
        if u['name'] == username and u['password'] == password:
            return True
    return False


# Let's say you want to create a user and take metadata (undefined amount of arguments)
#need to insert positional data first and then arbritary lists
def createUser(users,password):
    # create empty dictionary
    user = {}
    # populate with whatever was supplied
    user["username"] = users
    user["password"] = password