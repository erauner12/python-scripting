#!/usr/bin/python3.6
#nothing
print("")


#functions

#create first function:
def sayHello():
    print("Hello")

sayHello()

print("--")


usernames = [
    {
        'name'      :'bcranston',
        'priv'      :'admin',
        'password'  :'millennium'
    },
        {
        'name'      :'agunn',
        'priv'      :'user',
        'password'  :'abc123'
    }
]

#create authenticate function to take arguments of username and password
def authenticate(username,password):
    for u in usernames:
        if u['name'] == username and u['password'] == password:
            return True
    return False

#call the function to verify it works
if authenticate('bcranston','millennium'):
    print("Welcome!")
else:
    print("Sorry, wrong or non-existent credentials")

print("--")

#call it again, designate which variables you are passing in. By doing it this way, position of arguments do not matter
#flip the values to test this
if authenticate(password = 'phonypassword',username = 'phonyuser'):
    print("Welcome!")
else:
    print("Sorry, wrong or non-existent credentials")










