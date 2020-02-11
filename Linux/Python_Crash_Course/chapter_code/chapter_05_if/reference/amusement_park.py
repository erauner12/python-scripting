age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20

#python does not need an else block (else is a catch all statement)
#you can omit it to ensure that your code only takes data it expects to see

print(f"Your admission cost is ${price}.")
