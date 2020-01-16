age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")


# and operator
print("---")
# one condition to be true
age = 19
age < 21
# true

age <= 21
# true

age > 21
# false

age >= 21
# false

print("---")
# two conditions to be true

# and operator
age_0 = 22
age_1 = 18

age_0 >= 21 and age_1 >= 21
# false

age_0 = 21
age_1 = 21

age_0 >= 21 and age_1 >= 21
# true




# or operator
# one of the conditions to be true
age_0 = 22
age_1 = 18

verdict1 = age_0 >= 21 or age_1 >= 21
print(verdict1)
# true


age_0 = 18
verdict2 = age_0 >= 21 or age_1 >= 21
print(verdict2)
# false


