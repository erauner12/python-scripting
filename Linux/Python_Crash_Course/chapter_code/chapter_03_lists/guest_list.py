
guest_list = ['frank sinatra','rickie fowler','travis barker']

num_of_guests = len(guest_list)
print(f"We will be having {num_of_guests} guests tonight")

print(f"I will be inviting you, {guest_list[0].title()}, to my house for dinner")
print(f"I will be inviting you, {guest_list[1].title()}, to my house for dinner")
print(f"I will be inviting you, {guest_list[2].title()}, to my house for dinner")

print("---")
# last item in list
print(f"Unfortunately, {guest_list[-1].title()} is unable to make it")

popped_guest = guest_list.pop()

# calling the item that you removed
print(f" {popped_guest.title()} will not be joining us for dinner")

print("Here is the current list of people coming now:")
print(f"I will be inviting you, {guest_list[0].title()}, to my house for dinner")
print(f"I will be inviting you, {guest_list[1].title()}, to my house for dinner")

print("------")


print("Good new, more guests! We got a bigger table")

# insert at beginning
guest_list.insert(0,"michael jordan")
print(guest_list)

# insert in middle
guest_list.insert(2,"Michael Jackson")
print(guest_list)
# insert at the end
guest_list.append("ibraham mousus")
print(guest_list)

print(f"I will be inviting you, {guest_list[0].title()}, to my house for dinner")
print(f"I will be inviting you, {guest_list[1].title()}, to my house for dinner")
print(f"I will be inviting you, {guest_list[2].title()}, to my house for dinner")
print(f"I will be inviting you, {guest_list[3].title()}, to my house for dinner")
print(f"I will be inviting you, {guest_list[4].title()}, to my house for dinner")


print("------")

print("The dinner table will not arrive in time, we can only ivite two people")

starting_list = guest_list
print(starting_list)

first_remove = starting_list.pop()
print(f"removed {first_remove.title()}")

second_remove = starting_list.pop()
print(f"removed {second_remove.title()}")

third_remove = starting_list.pop()
print(f"removed {third_remove.title()}")

print(starting_list)
print(f"you are still coming, {guest_list[0].title()}, to my house for dinner")
print(f"you are still coming, {guest_list[1].title()}, to my house for dinner")

del guest_list[-1]

print(guest_list)

del guest_list[-1]

print(guest_list)

