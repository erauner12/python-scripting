#!/usr/bin/python3.6
print("")


#change

#lists = arrays in other programming languages
users = ["user1","user2","user3"]

#longway
#print (users[len(users) - 1])

#short way
print(users[-1])

#assign new value to list

#assigns jdoe to first variable in list
users[-1] = "jdoe"

#appends a new entry to list
users.append("pparker")
users.append("jane")
users.append("jake")
users.append("John")


#insert at a specific index
users.insert(0,"mary")

#pop method removes the last item in the list
users.pop()
removed = users.pop()
#if you wanted to remove the last item in the list, you would used this
#removed = users.pop()

#loop through array until the following item is removed
users.remove("jane")

#print list
print(users)

print("Removed User:",removed)










