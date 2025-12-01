# Basic Airthmatic
# Given:
# a = 15
# b = 4

# Task:
# Print the result of:
# 1. a + b
# 2. a - b
# 3. a * b
# 4. a / b
# 5. a // b
# 6. a % b
# 7. a ** b

# print(a +b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)


# 2️⃣ Comparison Operators
# # Given:
# x = 10
# y = 15

# Task:
# Print results of:
# x > y
# x < y
# x == y
# x != y
# x >= y
# x <= y

# print(x < y)
# print(x > y)
# print(x == y)
# print(x != y)
# print(x >= y)
# print(x <= y)


# 3️⃣ Logical Operators
# Given:
# age = 18
# has_id = False

# Task:
# Print True if user can vote (age >= 18 AND has_id)
# if age >= 18 and has_id:
#     print("true")
# else:
#     print("false")

# Print False otherwise


# 4️⃣ Assignment Operators
# Given:
# num = 10

# Task:
# Update num using compound assignment operators in this order:
# += 5
# -= 3
# *= 2
# //= 4
# Print value at each step.
# num += 5
# print(num)
# num -= 3
# print(num)
# num *= 2
# print(num)
# num //= 4
# print(num)



# 5️⃣ Membership Operators
# # Given:
# text = "python"
# lst = [1, 2, 3, "python"]

# Task:
# Check if:
# 'p' is in text
# 'on' is in text
# "python" is in lst
# 10 is not in lst

# if "p" in text:
#     print("True")

# if "on" in text:
#     print("True")

# if "python" in lst:
#     print("True")

# if 10 in lst:
#     print("True")


# 7️⃣ String Operator Practice
# # Given:
# s1 = "Hello"
# s2 = "Python"

# Task:
# Use operators to build: "Hello Python Python"
# print(s1 + " " + (s2 + " ")* 2)
# (Hint: concatenation + repetition operator *)


# 8️⃣ Mixed Data Type Operations
# Task:
# Evaluate and print the result + data type of:

# expr1 = 10 + 10.5     # int + float
# expr2 = "5" * 3       # string * int
# expr3 = True + 5      # bool + int
# expr4 = False * 10    # bool * int

# print("expr1 " + str(expr1)+ " -> ", type(expr1))
# print("expr2 " + str(expr2)+" -> ", type(expr2))
# print("expr3 " + str(expr3)+" -> ", type(expr3))
# print("expr4 " + str(expr4)+" -> ", type(expr4))

# 9️⃣ Bitwise Operators


# # Given:
# x = 10     # binary 1010
# y = 4      # binary 0100

# Task:
# # Calculate:
# print(x & y)
# print(x | y)
# print(x ^ y)
# print(x << 2)
# print(y >> 1)


# 🔟 Complex Condition + Input + Operators

# Task:
# Take input for:
# marks (int)
# attendance_percentage (float)

# Eligibility rule:
# student can sit in exam if:
# marks >= 35 AND (attendance >= 75 OR marks > 90)

# Print True or False


marks = int(input("Enter marks: "))
attendance_percentage = float(input("attendance percentage: "))

if marks >= 35 and (attendance_percentage >= 75 or marks > 90):
    print("True")
else:
    print("False")
