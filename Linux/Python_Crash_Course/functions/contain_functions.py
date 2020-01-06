#!/usr/bin/python3.6


# The triple quotes is called a docstring, needed to help describe what the function is doing
def greet_user(username):
    """Greetings!"""
    print("Hello " + username.title())

# functions have parameters which require arguments when they are called
def display_message(answer):
    """Displaying answer to question of what the user is learning this chapter"""
    print("Good to know that you are learning " + answer)


def favorite_book(book):
    """Displaying the user's favorite book"""
    print("One of you favorite books is: " + book)



