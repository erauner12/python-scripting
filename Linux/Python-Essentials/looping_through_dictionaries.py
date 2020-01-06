#!/usr/bin/python3.6
# nothing
print("")

import user_functions


users = [
    {
        'name'      :'bcranston',
        'password'  :'millennium'
    },
        {
        'name'      :'agunn',
        'password'  :'abc123'
    }
]



# call function
if user_functions.authenticate(username = 'name',password = 'phonypassword'):
    print("Welcome!")
else:
    print("Sorry, wrong or non-existent credentials")



#dictionary key pairs allow us to add as many arguments as we want to a dictionary
user_functions.createUser("Evan","password123")

print(users)
    #use dictionary instead












