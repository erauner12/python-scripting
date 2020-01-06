#!/usr/bin/python3.6

users = {
    'Evan' : {
        'first' : 'Evan',
        'last' : 'Rauner',
        'location': 'KC',
    },
    'Jake' : {
        'first' : 'Jake',
        'last' : 'Herburger',
        'location' : 'Tulsa',
    },
}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    print("Full Name: " + full_name.title())
    print("Location: " + location.title())
    

    



