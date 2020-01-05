#!/usr/bin/python3.6

#Store information about a pizza that is being ordered

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

#summarize the order

print("You just ordered a " + pizza['crust'] + "-crust pizza " + "with the following toppings:")

for topping in pizza["toppings"]:
    print("\t " + topping)



