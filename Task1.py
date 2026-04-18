# TASK 1: Student Marks Dictionary

# 1. Create a dictionary of 3 students with their marks
students = {"Ali": 80, "Sara": 90, "Ahmed": 75}

# 2. Print all student names
print("Student Names:")
for name in students.keys():
    print(name)

# 3. Print all marks
print("Marks:")
for marks in students.values():
    print(marks)

# 4. Find student with highest marks
highest = max(students.values())
print("Highest Marks:", highest)
for name in students:
    if students[name] == highest:
        print("Top Student:", name)