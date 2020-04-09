favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }


print("---------")

sarah_language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {sarah_language}.")


print("---------")

#Here is how you print out both items in a dictionary:

for name,language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")

print("---------")

# How you loop through all the values instead of they keys

print("the following languages have been mentioned:")

for language in favorite_languages.values():
    print(language.title())

    
print("---------")

# How you would sort functio the keys/value of output

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()},Thank you for taking the poll")

print("---------")
# how you remove duplicates by using set function

for language in set(favorite_languages.values()):
    print(f"{language.title()} is in the list")



print("---------")

#finally here is a set
#similiar to a list but more like a dictionary. Looks like a dictionary because of the curly braces but there are no key value pair

print(f"Here is a set")

languages = {'python','ruby','python','c'}
print(languages)


print("---------")

#this is how you print out keys

friends = ['phil', 'sarah']
#printing through keys is the default behavior for example
# this would accomplish the same thing
#for name in favorite_languages:
for name in favorite_languages.keys():
    print(name.title())
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")



