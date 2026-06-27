# MODULE 8 - ADVANCED PYTHON
# LESSON 3 - OBJECT ORIENTED PROGRAMMING 1
# ACTIVITY - Class Student - 2

class Student:
    grade = 12
    name = "Abhishek"

    def introduction(self):
        print("Hi I am a student")

    def details(self):
        print("My name is", self.name)
        print("I study in Grade", self.grade)


ob = Student()
ob.introduction()
ob.details()
