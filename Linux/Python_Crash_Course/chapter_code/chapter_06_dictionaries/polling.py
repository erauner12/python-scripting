

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }


taken_poll = ['sarah','edward']
for name in favorite_languages.keys():
    print(f"{name.title()} should take the language poll")

    if name in taken_poll:
        language = favorite_languages[name].title()
        print(f"{name.title()} already took the poll and chose {language}, thank you")


