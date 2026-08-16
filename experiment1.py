# Experiment 01: Simple Python program using operators and basic constructs
# Course: Basic Python Programming
# Title: Python Operators, Data Types, and Control Flow

# ----------------------------------------------------
# 1. Variables & Basic Input/Output
# ----------------------------------------------------
print("=== Basic Variables and Statements ===")

# Variable assignment
x = 10
y = 3.14
z = "Python"

print("Values:", x, y, z)
print("Type of x:", type(x))
print("Type of y:", type(y))
print("Type of z:", type(z))

# Multiple variable assignment
a, b, c = 10, 20, 30
print("a, b, c:", a, b, c)

# Variable ID / Address check
p = 100
q = p
print("Address of p:", id(p))
print("Address of q:", id(q))


# ----------------------------------------------------
# 2. Operators in Python
# ----------------------------------------------------
print("\n=== Demonstration of Operators ===")

num1 = 15
num2 = 4

# a) Arithmetic Operators
print("\n-- Arithmetic Operators --")
print("Addition (15 + 4):", num1 + num2)
print("Subtraction (15 - 4):", num1 - num2)
print("Multiplication (15 * 4):", num1 * num2)
print("Division (15 / 4):", num1 / num2)
print("Floor Division (15 // 4):", num1 // num2)
print("Modulus (15 % 4):", num1 % num2)
print("Exponentiation (15 ** 4):", num1 ** num2)

# b) Relational (Comparison) Operators
print("\n-- Relational Operators --")
print("15 > 4:", num1 > num2)
print("15 < 4:", num1 < num2)
print("15 == 4:", num1 == num2)
print("15 != 4:", num1 != num2)
print("15 >= 4:", num1 >= num2)
print("15 <= 4:", num1 <= num2)

# c) Logical Operators
print("\n-- Logical Operators --")
val1 = True
val2 = False
print("val1 and val2:", val1 and val2)
print("val1 or val2:", val1 or val2)
print("not val1:", not val1)

# d) Bitwise Operators
print("\n-- Bitwise Operators --")
n1 = 10  # in binary: 1010
n2 = 4   # in binary: 0100
print("Bitwise AND (10 & 4):", n1 & n2)
print("Bitwise OR (10 | 4):", n1 | n2)
print("Bitwise XOR (10 ^ 4):", n1 ^ n2)
print("Bitwise NOT (~10):", ~n1)
print("Right Shift (10 >> 2):", n1 >> 2)
print("Left Shift (10 << 2):", n1 << 2)

# e) Assignment Operators
print("\n-- Assignment Operators --")
m = 10
print("Initial m:", m)
m += 5
print("m += 5:", m)
m -= 3
print("m -= 3:", m)
m *= 2
print("m *= 2:", m)

# f) Identity Operators
print("\n-- Identity Operators --")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 is list3:", list1 is list3)
print("list1 is list2:", list1 is list2)
print("list1 is not list2:", list1 is not list2)

# g) Membership Operators
print("\n-- Membership Operators --")
sample_list = [10, 20, 30, 40, 50]
check_val1 = 20
check_val2 = 99

print("20 in sample_list:", check_val1 in sample_list)
print("99 not in sample_list:", check_val2 not in sample_list)

# h) Ternary Operator
print("\n-- Ternary Operator --")
a_val = 10
b_val = 20
min_value = a_val if a_val < b_val else b_val
print("Smaller value between 10 and 20 is:", min_value)


# ----------------------------------------------------
# 3. Data Types & Keywords
# ----------------------------------------------------
print("\n=== Data Types and Keywords ===")

# Basic Data Types
s_str = "MIT WPU"
l_list = [10, 20, "Pune"]
t_tuple = (1, 2, 3)
d_dict = {1: "One", 2: "Two"}
set_var = {1, 2, 3, 3, 2}

print("String:", s_str)
print("List element:", l_list[0])
print("Tuple element:", t_tuple[1])
print("Dictionary get:", d_dict.get(1))
print("Set (unique values):", set_var)

# Keywords check
import keyword
print("Total Keywords in Python:", len(keyword.kwlist))


# ----------------------------------------------------
# 4. Control Statements & Loops
# ----------------------------------------------------
print("\n=== Control Flow and Loops ===")

# Decision making: If-Elif-Else
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: Fail")

# For loop demonstration
print("\nFor loop using range:")
for i in range(1, 5):
    print(i, end=" ")
print()

# Break, Continue, Pass
print("\nLoop Control (Break & Continue):")
colleges = ["MIT", "WPU", "Pune", "Engineering"]

print("Using Break at 'Pune':")
for col in colleges:
    if col == "Pune":
        break
    print(col, end=" ")
print()

print("Using Continue at 'Pune':")
for col in colleges:
    if col == "Pune":
        continue
    print(col, end=" ")
print()

# Pass statement usage
n_test = 10
if n_test > 5:
    pass  # Placeholder for future logic
