# Experiment 02: Python Conditional Statements and Loops
# Course: Basic Python Programming
# Title: Decision-Making, Loops, Pattern Building, and Algorithms

# ----------------------------------------------------
# 1. Decision Making (If, If-Else, If-Elif-Else, Nested If)
# ----------------------------------------------------
print("=== 1. CONDITIONAL STATEMENTS ===")

# Simple if
num = 10
if num > 0:
    print("Positive number")

# if-else
num = -5
if num >= 0:
    print("Positive number")
else:
    print("Negative number")

# if-elif-else ladder
score = 85
if score >= 90:
    print("Grade: A+")
elif score >= 75:
    print("Grade: A")
elif score >= 60:
    print("Grade: B")
else:
    print("Grade: C")

# Nested if-else
num = 15
if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Number is zero or negative")

# Largest of Three Numbers (DSA Comparison Example)
a, b, c = 10, 25, 15
if a > b:
    if a > c:
        largest = a
    else:
        largest = c
else:
    if b > c:
        largest = b
    else:
        largest = c
print(f"Largest among {a}, {b}, {c} is:", largest)

# Even-Odd & Divisibility Check
num = 30
if num % 2 == 0:
    if num % 5 == 0:
        print(f"{num} is Even and divisible by 5")
    else:
        print(f"{num} is Even but not divisible by 5")
else:
    print(f"{num} is Odd number")


# ----------------------------------------------------
# 2. Control Loops (For & While Loops)
# ----------------------------------------------------
print("\n=== 2. CONTROL LOOPS ===")

# Basic For Loop & Array Traversal
arr = [10, 20, 30, 40, 50]
total = 0
for val in arr:
    total += val
print("Sum of array elements:", total)

# Maximum Element in Array
arr_max = [12, 45, 23, 51, 19, 8]
max_val = arr_max[0]
for n in arr_max:
    if n > max_val:
        max_val = n
print("Maximum Element:", max_val)

# Linear Search
search_arr = [4, 7, 1, 9, 3]
key = 9
found = False
for val in search_arr:
    if val == key:
        found = True
        break
print("Linear Search Result:", "Element Found" if found else "Element Not Found")

# Factorial using For Loop
fact_n = 5
fact = 1
for i in range(1, fact_n + 1):
    fact *= i
print(f"Factorial of {fact_n}:", fact)

# Fibonacci Series
fib_n = 10
f1, f2 = 0, 1
print("Fibonacci Series:", end=" ")
for _ in range(fib_n):
    print(f1, end=" ")
    f1, f2 = f2, f1 + f2
print()

# Loop through Dictionary
student = {"name": "Mrunal", "age": 21, "marks": 92}
print("Student Details:")
for k, v in student.items():
    print(f"  {k}: {v}")

# String Reversal
string = "Python"
rev_str = ""
for ch in string:
    rev_str = ch + rev_str
print(f"Reversed '{string}':", rev_str)

# Palindrome Check
palindrome_num = "121"
if palindrome_num == palindrome_num[::-1]:
    print(f"'{palindrome_num}' is a Palindrome Number")
else:
    print(f"'{palindrome_num}' is Not a Palindrome")


# ----------------------------------------------------
# 3. Loop Control Statements (Break, Continue, Pass)
# ----------------------------------------------------
print("\n=== 3. LOOP CONTROL STATEMENTS ===")

# Continue Statement Example (Skip multiples of 3)
print("Numbers 1 to 10 skipping multiples of 3:", end=" ")
for num in range(1, 11):
    if num % 3 == 0:
        continue
    print(num, end=" ")
print()

# Pass Statement Example
print("Demonstrating pass statement:")
for letter in "PYTHON":
    if letter == "H":
        pass  # Placeholder
    print("Letter:", letter, end=" | ")
print()


# ----------------------------------------------------
# 4. Pattern Building Programs
# ----------------------------------------------------
print("\n=== 4. PATTERN BUILDING ===")

# Right-Angled Triangle Pattern
print("\nRight-Angled Triangle:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end="")
    print()

# Inverted Right-Angled Triangle
print("\nInverted Triangle:")
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Number Triangle Pattern
print("\nNumber Triangle:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# Pyramid Pattern
print("\nPyramid Pattern:")
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    print("* " * i)

# Alphabet Triangle Pattern
print("\nAlphabet Triangle:")
ch = 65  # ASCII for 'A'
for i in range(5):
    for j in range(i + 1):
        print(chr(ch), end=" ")
        ch += 1
    print()

# Floyd's Triangle
print("\nFloyd's Triangle:")
num_f = 1
for i in range(1, 6):
    for j in range(1, i + 1):
        print(num_f, end=" ")
        num_f += 1
    print()

# Diamond Pattern
print("\nDiamond Pattern:")
r = 4
for i in range(1, r + 1):
    print(" " * (r - i) + "* " * i)
for i in range(r - 1, 0, -1):
    print(" " * (r - i) + "* " * i)
