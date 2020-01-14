pizzas = ["pepperoni","barbecue chicken", "pineapple pizza"]

for pizza in pizzas:
    print(f"I like {pizza}")

print("I absolutely just love pizza")


# Now we have two different lists
friends_pizzas= pizzas[:]

pizzas.append("anchovy")
print(pizzas)

friends_pizzas.append("supreme")
print(friends_pizzas)