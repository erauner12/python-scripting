
numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number < 2:
        print(f"{number}st")
    elif number < 3 and number > 1:
        print(f"{number}nd")
    elif number < 4 and number > 2:
        print(f"{number}rd")
    else:
        print(f"{number}th")


