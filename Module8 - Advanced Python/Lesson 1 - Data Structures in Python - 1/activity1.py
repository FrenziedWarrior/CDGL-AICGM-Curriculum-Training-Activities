# MODULE 8 - ADVANCED PYTHON
# LESSON 1 - DATA STRUCTURES IN PYTHON 1
# ACTIVITY - SCHOOL CLASS ORGANISER

# TASK 1 - Create a list of classmates
classmates = ["Abhishek", "Rudra", "Alyan", "Gunjan", "Daksh"]

print("Class list:", classmates)

# TASK 2 - Access the list
print("Total students:", len(classmates))
print("First student:", classmates[0])
print("Last student:", classmates[-1])
print("First three:", classmates[:3])

# TASK 3 - Modify the list
classmates.append("Minerva")
print("\nAfter adding Minerva:", classmates)
classmates.remove("Rudra")
print("After removing Rudra:", classmates)
classmates.sort()
print("Sorted alphabetically:", classmates)
classmates.reverse()
print("Reversed:", classmates)

# TASK 4 - Create a Teacher dictionary
teacher = {
    "name": "Mr. Karmakar",
    "subject": "Python",
    "experience": 1
}
print("\nTeacher profile:", teacher)

# TASK 5 - Dictionary Operations
print("Subject:", teacher["subject"])
print("Experience:", teacher.get("experience", "Not Found"))
teacher["experience"] = 2
teacher["email"] = "karmakar@codingal.com"
teacher.pop("experience")
print("Updated teacher profile:", teacher)

# TASK 6 - Convert list to a student dictionary
roll_numbers = [1, 2, 3, 4, 5]
names = ["Abhishek", "Rudra", "Alyan", "Gunjan", "Daksh"]
student_directory = dict(zip(roll_numbers, names))
print("\nStudent Directory:", student_directory)
print("Student at Roll 3:", student_directory[3])
