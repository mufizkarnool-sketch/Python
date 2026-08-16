# Experiment 03: Python Lists and Tuples Operations
# Course: Basic Python Programming
# Title: Create, Access, Update, Delete operations on Lists and Tuples

# ----------------------------------------------------
# 1. PYTHON LISTS: Creation, Access, Update, Delete
# ----------------------------------------------------
print("=== 1. PYTHON LISTS ===")

# a) Create Lists
list_int = [1, 2, 3, 4, 5]
list_str = ['apple', 'banana', 'cherry']
list_mixed = [1, 'hello', 3.14, True]
print("Integer List:", list_int)
print("String List:", list_str)
print("Mixed List:", list_mixed)

# Creating list using list() constructor and range/comprehension
list_from_tuple = list((1, 2, 3, 'apple', 4.5))
list_from_str = list("MIT")
repeated_list = [2] * 5
print("List from tuple:", list_from_tuple)
print("List from string:", list_from_str)
print("Repeated list:", repeated_list)

# b) Accessing List Elements (Indexing & Slicing)
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print("First element (index 0):", nums[0])
print("Last element (index -1):", nums[-1])
print("Slice [1:4]:", nums[1:4])
print("Slice with step [::2]:", nums[::2])
print("Reversed list using slicing [::-1]:", nums[::-1])

# c) Adding / Updating Elements (Mutable nature)
# Using append, extend, insert
my_list = []
my_list.append(10)
my_list.insert(0, 5)
my_list.extend([15, 20, 25])
print("After append, insert, extend:", my_list)

# Updating by index
my_list[1] = 25
print("After updating index 1 to 25:", my_list)

# d) Deleting Elements from List
# remove(), pop(), del
sample_list = [10, 20, 30, 40, 50, 30]
sample_list.remove(30) # removes first occurrence
print("After remove(30):", sample_list)

popped_val = sample_list.pop() # removes last element
print("Popped value:", popped_val)
print("After pop():", sample_list)

del sample_list[0]
print("After del sample_list[0]:", sample_list)

# List Methods
print("Count of 2 in [1, 2, 3, 2]:", [1, 2, 3, 2].count(2))
sort_demo = [3, 1, 2]
sort_demo.sort()
print("Sorted list:", sort_demo)

# List Comprehension
squares = [x**2 for x in range(1, 6)]
print("List Comprehension Squares:", squares)


# ----------------------------------------------------
# 2. PYTHON TUPLES: Creation, Access, Immutability
# ----------------------------------------------------
print("\n=== 2. PYTHON TUPLES ===")

# a) Create Tuples
empty_tuple = ()
numbers_tuple = (10, 20, 30, 40)
mixed_tuple = (10, "Hello", 3.14, True)
implicit_tuple = 1, 2, 3, 4 # Tuple without parentheses
single_element_tuple = (10,) # Comma is mandatory

print("Empty Tuple:", empty_tuple)
print("Numbers Tuple:", numbers_tuple)
print("Single Element Tuple:", single_element_tuple, type(single_element_tuple))

# b) Accessing Tuple Elements & Slicing
colors = ("red", "green", "blue", "yellow", "purple")
print("First color:", colors[0])
print("Colors slice [0:3]:", colors[0:3])
print("Colors negative index slice [-3:]:", colors[-3:])

# c) Tuple Operations (Concatenation & Repetition)
t1 = (1, 2, 3)
t2 = (4, 5, 6)
combined = t1 + t2
repeated = t1 * 2
print("Concatenated Tuple:", combined)
print("Repeated Tuple:", repeated)

# d) Modifying / Deleting Tuples (Converting to List and back)
# Tuples are immutable, so to modify elements, convert to list first
tuple_data = (1, 2, 3, 4)
list_data = list(tuple_data)
list_data.append(5)
tuple_data = tuple(list_data)
print("Modified tuple via list conversion:", tuple_data)
