#!/usr/bin/python3.6

"This is a string"
'This is also a string'

'I told my friend, "Python is my favorite language!"'

"I told my friend, 'Python is my favorite language!'"

#Notice how the apostrophe is fine in the middle because we are using double quotes
message = "One of Python's strengths is its diverse community."



#combining or concatencating strings:

first_name = "evan"
last_name = "rauner"

full_name = first_name + " " + last_name

#print variable
print(full_name)
print("------")

#assign new concatenated sentence to new variable and print it
message = "Hello, " + full_name.title() + "!"

print(message)
print("------")


#tab character
print("\t" + "tabbed")
print("------")

#newline character
print("\nNew Line\n")
print("------")








