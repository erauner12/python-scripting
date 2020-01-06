#!/usr/bin/python3.6
print("")



users = ["parker","jane","jake"]

#lists = arrays in other programming languages
userList1 = []
userList2 = []

#appends a new entry to list
userList1.append("parker")
userList1.append("jane")
userList1.append("jake")

userList2.append("parker")
userList2.append("jane")
userList2.append("jake")


num = "123"


#easy to change items in list this way
for i in range(0,len(userList1)):
    userList1[i] = userList1[i] + num
    print(userList1[i])

print("--")

#more traditional loop, more complicated than what is above
for u in userList2[0:len(userList2)]:
    u = u + num
    userList2.append(u)
    print(u)

print("--")

#List comprehension first example
users = [u + num for u in users]
print(users)

print("--")

#string is just a list of characters
message = "Hello World"

'''
for s in message:
    print(s) 
'''

#adding a space in between every letter of the string we are turning into a list
message = [s + " " for s in message]
#applying join to the list we just made to print the string with a space in between every character
print(''.join(message))

print("--")

#this accomplishes the same thing
message2 = "Hello World"
print(' '.join(message2))











