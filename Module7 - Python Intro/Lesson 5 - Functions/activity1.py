def intro(name):
    """
        Write a Python program that takes a name as an input from the user 
        and then creates a function that accepts the same name 
        as a parameter and introduces the user.
    """
    print("Hello, Good morning! I am", name)

user_name = input("Enter your name: ")
intro(user_name)