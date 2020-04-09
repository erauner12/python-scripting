#user_names = ['dr1nk182','brittyboy','riotmaker','beercules','admin']

user_names = []


if user_names:
    for user in user_names:
        if user == 'admin':
            print(f"Hello {user}, would you like to see some reports")
        else:
            print(f"Hello {user}, thank you for logging in again")
else:
    print("We need to find some users!")
