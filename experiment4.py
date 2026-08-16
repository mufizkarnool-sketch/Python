# Experiment 04: Python Sets and Dictionaries Operations
# Course: Basic Python Programming
# Title: Create, Access, Update, Delete, and Looping Operations on Sets & Dictionaries

# ----------------------------------------------------
# 1. PYTHON SETS: Creation, Access, Update, Delete & Mathematical Operations
# ----------------------------------------------------
print("=== 1. PYTHON SETS ===")

# a) Create Sets
numbers = {10, 20, 30, 40, 50}
print("Set using literal:", numbers)
print("Type:", type(numbers))

# Creating set using set() constructor
num_set = set([10, 20, 30, 40, 50])
letters = set("PYTHON")
print("Set using set() constructor:", num_set)
print("Set from string:", letters)

# b) Accessing Set Elements (Membership testing & Iteration)
print("
-- Accessing Set Elements --")
print("Is 30 present in set?", 30 in numbers)
print("Is 100 present in set?", 100 in numbers)

print("Iterating through set:")
for x in numbers:
    print(x, end=" ")
print()

# c) Adding and Updating Set Elements
print("
-- Adding & Updating Set Elements --")
s = {10, 20, 30}
print("Original set:", s)
s.add(40)
print("After add(40):", s)
s.update([50, 60, 70])
print("After update([50, 60, 70]):", s)

# d) Deleting Set Elements
print("
-- Deleting Set Elements --")
del_set = {10, 20, 30, 40, 50}
print("Original set:", del_set)

del_set.remove(30)
print("After remove(30):", del_set)

del_set.discard(40)
print("After discard(40):", del_set)

popped_item = del_set.pop()
print(f"After pop() [removed {popped_item}]:", del_set)

del_set.clear()
print("After clear():", del_set)

# e) Set Operations (Union, Intersection, Difference, Symmetric Difference)
print("
-- Mathematical Set Operations --")
set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}
print("Set 1:", set1)
print("Set 2:", set2)
print("Union (set1 | set2):", set1 | set2)
print("Intersection (set1 & set2):", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
print("Symmetric Difference (set1 ^ set2):", set1 ^ set2)


# ----------------------------------------------------
# 2. PYTHON DICTIONARY: Creation, Access, Update, Delete & Looping
# ----------------------------------------------------
print("
=== 2. PYTHON DICTIONARY ===")

# a) Create Dictionary
student = {
    "name": "Rahul",
    "roll_no": 101,
    "branch": "CSE",
    "percentage": 85.5
}
print("Student Dictionary:", student)
print("Type:", type(student))

# b) Accessing Dictionary Elements
print("
-- Accessing Elements --")
print("Name (using []):", student["name"])
print("Roll No (using []):", student["roll_no"])
print("Branch (using get()):", student.get("branch"))
print("Percentage (using get()):", student.get("percentage"))

# c) Updating Dictionary Elements
print("
-- Updating & Adding Elements --")
student["percentage"] = 90.5  # Updating existing value
student["city"] = "Pune"       # Adding new key-value pair
print("Updated Dictionary:", student)

# d) Deleting Dictionary Elements
print("
-- Deleting Elements --")
del_dict = student.copy()

del del_dict["branch"]
print("After del branch:", del_dict)

popped_val = del_dict.pop("percentage")
print(f"After pop('percentage') [removed {popped_val}]:", del_dict)

popped_item = del_dict.popitem()
print(f"After popitem() [removed {popped_item}]:", del_dict)

del_dict.clear()
print("After clear():", del_dict)

# e) Looping Through Dictionary
print("
-- Looping Through Dictionary --")
print("Keys:")
for key in student:
    print(key, end=" ")
print()

print("
Values:")
for value in student.values():
    print(value, end=" ")
print()

print("
Key-Value Pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")

# f) Practical Application: Student Marks Analysis
print("
-- Practical Application: Student Marks Analysis --")
marks = {
    "Python": 85,
    "Data Structure": 90,
    "Database": 78,
    "Computer Network": 88
}

print("Subject-wise Marks:")
for subject, mark in marks.items():
    print(f"  {subject}: {mark}")

total_marks = sum(marks.values())
avg_marks = total_marks / len(marks)
print("Total Marks:", total_marks)
print("Highest Marks:", max(marks.values()))
print(f"Average Marks: {avg_marks:.2f}")
