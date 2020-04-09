current_users = ['Dr1nk182','Brittyboy','Riotmaker','Beercules','Admin']
lowercase_users = []

for current_user in current_users:
    lowercase_users.append(current_user.lower)



new_users = ['user1','dr1nk182','user2','riotmaker','user3']


for new_user in new_users:
    if new_user in lowercase_users:
        print(f"the username {new_user} is already in use")
    else:
        print(f"the username {new_user} is available")


    


