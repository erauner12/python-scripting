#!/usr/bin/python3.6
#nothing
print("")

print("--")

#create default password for every user
password = "pass123"

#user needs to speak a language
lang = {
    "en":"English",
    "es":"Spanish",
    "ar":"Arabic",
    "it":"Italian"
}

#create list of dictionaries
users = [
    {"username":"Evan","job":"devops engineer"},
    {"username":"Jake","job":"dba"},
    {"username":"John","job":"sysadmin"}
]

#loop through every user and assign the string "pass123" to every users's password key
for i in range(0,len(users)):
    users[i]['password'] = 'Pass123'

#delete the password field of every user, using the del method
''' for i in range(0,len(users)):
    del(users[i][password]) '''



#we have looped through lists before, but here is how you loop through a dictionary

#loop through just the key
for k in lang:
    print(k)

print("--")

#loop through both key and value
for key,value in lang.items():
    print(key,value)






#create user
user = {"username":"John","job":"sysadmin"}

#change job dictionary key to tester:
user["job"] = "tester"

#add new item to the dictionary:
user["password"] = "pass123"

#print(user)



 






















#nothing
print("")
print("")
#nothing

