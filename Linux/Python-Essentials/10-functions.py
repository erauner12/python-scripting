#!/usr/bin/python3.6


def authenticate(username,password,users):
    for u in usernames:
        if u['name'] == username and u['password'] == password:
            return True
    return False


def createUser(usernames,password,**meta):
    # create empty dictionary
    user = {}
    # populate with whatever was supplied
    user["username"] = usernames
    user["password"] = password