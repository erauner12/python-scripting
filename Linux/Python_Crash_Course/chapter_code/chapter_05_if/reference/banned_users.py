
# checking if an item is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")



# checking if an itme is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']

is_mushrooms = 'mushrooms' in requested_toppings
print(is_mushrooms)
# true


is_pepperoni = 'pepperoni' in requested_toppings
print(is_pepperoni)
# false