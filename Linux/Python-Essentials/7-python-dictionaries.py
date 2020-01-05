#!/usr/bin/python3.6
#nothing
print("")

#tuples (data structure)
#tuples cannot be changed like a list

priv = ("user","admin")
for p in priv:
    print(p)

print("--")

#Here is the difference between a tuple and a dictionary
user = 'jdoe','31','Devops Engineer','US'

#dictionaries - accepts items as key value pair
user = {
    "username":"jdoe",
    "age":"31",
    "job":"DevOps Engineer",
    "country":"USA"
}

#print("The username is",user["username"," he is",user["job"],"who lives in ",user["country"])

print("The username is",user["username"],"He is",user["age"],"year old.\nHe works as a",user["job"], "in",user["country"])


#create list of dictionaries

users = [
    {"username":"Evan","job":"devops engineer"},
    {"username":"Jake","job":"dba"},
    {"username":"John","job":"sysadmin"}
]


#loop through it

for u in users:
    print ("His name is",u["username"],"and he is a",u["job"])























#nothing
print("")
print("")
#nothing

