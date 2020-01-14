
slice_list = ["one","two","three","four","five"]

print(f"the first three items in the list are: ")

for single_slice_1 in slice_list[:3]:
    print(single_slice_1.title())


print("---")

print(f"the first three items in the middle of the list are: ")

for single_slice_2 in slice_list[1:4]:
    print(single_slice_2.title())

print("---")


for single_slice_3 in slice_list[-3:]:
    print(single_slice_3.title())
