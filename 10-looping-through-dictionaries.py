#!/usr/bin/python3.6
# nothing
print("")


# functions

# create first function:
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

# create authenticate function to take arguments of username and password
#adding an additional parameter. Defaulting it to user. Ensures that the function calling it will have something to put in if nothing is supplied
#this is acalled an optional argument
def authenticate(username,password,priv="user"):
    for u in usernames:
        if u['name'] == username and u['password'] == password:
            return True
    return False



# call function
# mixing both positional arguments and inserted the others in regardless of order
#*Need to put the positional argument first since it is called first
if authenticate(password = 'phonypassword',username = 'phonyuser',priv="admin"):
    print("Welcome!")
    print("Your privelege is",)
else:
    print("Sorry, wrong or non-existent credentials")


# Let's say you want to create a user and take metadata (undefined amount of arguments)
#need to insert positional data first and then arbritary lists
def createUser(usernames,password,**meta):
    # create empty dictionary
    user = {}
    # populate with whatever was supplied
    user["username"] = usernames
    user["password"] = password

#adding items method to dictionary to enable us to loop through it
#each value in the key pair is being assigned for every additional argument that was not gathered before
    for k,v in meta.items():
        user[k] = v
    return user

#dictionary key pairs allow us to add as many arguments as we want to a dictionary
user = createUser("Evan","password123",job = "Devops Engineer", age = "26", country = "US", lang = "English")

print(user)
    #use dictionary instead












