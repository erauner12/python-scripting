#!/usr/bin/python3.6
print("")

# if conditions
''' 
== equal to
> greater than
> greater than or equal to
< less
< less than or equal to
'''

#if one is greater than two, then something is wrong
if 1 > 2:
    print("Something is wrong")
else:
    print("That is correct")

print("--")

#equal to or not equal to
if 1 == 1:
    print("That is correct")

if 1 != 1:
    print("These are not equal")

print("--")

username = 'jdoe'
password = 'pass123'
usernames= ['jdoe','linda','evan','jake']

if username == 'jdoe' and 'pass123':
    print("Login Succesful, Welcome",username)
else:
    print("Sorry, wrong username or password")

print("--")

