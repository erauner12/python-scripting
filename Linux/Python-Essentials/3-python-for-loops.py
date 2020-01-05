#!/usr/bin/python3.6
print("")




#lists = arrays in other programming languages
users = []

#appends a new entry to list
users.append("parker")
users.append("jane")
users.append("jake")
users.append("brian")
users.append("kris")

#print in order that list was populated
print(users)

#create variable for sorted_list and then print it
sorted_users = (sorted(users))
print(sorted_users)
print("--")

#in python, code blocks are defined using colons
for u in users:
    print("Username is",u.title())
print("--")

#this will print the range of the starting index in the list to the length of the users which is the last item in the list
for i in range(0,len(users)):
    print(users[i])

print("--")

#same thing, but capitalizes first letter of every item in the list
for i in range(0,len(users)):
    users[i] = users[i].title()
    print(users[i])

print("--")

#shorthand way of grabbing all members of an array, without designated the end of the array
all_users = users[0:]
print(all_users)

print("--")

#print everything to the 3rd index in the list
almost_all_users = users[:3]
print(almost_all_users)

#everything up to index in the list
print(users[:2])
#and so on
print(users[:1])

