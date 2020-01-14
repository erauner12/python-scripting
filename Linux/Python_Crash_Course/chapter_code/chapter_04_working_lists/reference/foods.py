# This is how you copy a list to another list
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]

# This does not work, the lists become the same if we do this:
#friend_foods = my_foods


my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
#print(my_foods)

for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
#print(friend_foods)

for friend_food in friend_foods:
    print(friend_food)


