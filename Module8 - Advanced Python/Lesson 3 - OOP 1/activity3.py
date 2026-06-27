# MODULE 8 - ADVANCED PYTHON
# LESSON 3 - OBJECT ORIENTED PROGRAMMING 1
# ACTIVITY - Parrot Bird

class Parrot:
    # Class attribute
    species = "bird"

    # Instance attribute
    def __init__(self, name, age):
        self.name = name
        self.age = age


# TASK 1 - Instantiate the Parrot class
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# TASK 2 - Access the class attributes
print("Blu is a {}".format(blu.species))
print("Woo is also a {}".format(woo.species))

# TASK 3 - Access the instance attributes
print("{} is {} years old".format(blu.name, blu.age))
print("{} is {} years old".format(woo.name, woo.age))
