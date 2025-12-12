
# 1️⃣ Positive, Negative, or Zero
# Concepts: basic if–elif–else, comparisons
# Problem:
# Given an integer x, print:
# "Positive" if x > 0
# "Negative" if x < 0
# "Zero" otherwise

# x = 6
# if x > 0:
#     print("Positive")
# elif x < 0:
#     print("Negative")
# else:
#     print("zero")

# 2️⃣ Even or Odd
# Concepts: modulo %, boolean condition
# Problem:
# Given an integer n, print "Even" if it’s divisible by 2, else "Odd".

# n = 23

# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# 3️⃣
# Write a program that compares two numbers and prints:
# which one is larger, or
# that both are equal.

# a = 5 
# b = 6

# if a > b:
#     print (f"{a} is larger than {b}")
# elif b > a:
#     print(f"{b} is larger than {a}")
# else:
#     print("both are equal")


# 4️⃣
# Write a program that takes marks (0–100) and prints the grade:
# A, B, C, D, or Fail.
# Print "Invalid" if marks are outside the range.

# marks = int(input("Enter your marks: "))

# if marks >= 0 and marks <=100:
#     if marks >= 90:
#         print("you got Grade : A")
#     elif marks >= 75:
#         print("you got grade: B")
#     elif marks >= 60:
#         print("you got grade: C")
#     elif marks >= 40:
#         print("you got grade D")
#     else: 
#         print("you did't pass the exam. (Fail)")
# else:
#     print("INVALID")


# 5 Write a program that checks whether a person can vote, given age and citizen (True/False).

# age = 55
# citizen = True

# if age >= 18 and citizen == True:
#     print("The person can vote.")

# 6️⃣ Leap Year Check
# Concepts: multiple logical rules
# Problem:
# Given a year:
# Leap year if divisible by 400

# OR divisible by 4 AND not divisible by 100
# Otherwise not leap year.


# given_year = 2000

# if (given_year % 4 == 0 and given_year % 100 != 0) or given_year % 400 == 0:
#     print(f"The given year {given_year} is a leap year.")
# else:
#     print(f"The given year {given_year} is not a leap year")


# 7️⃣ Login System

# Concepts: nested if, string comparison
# Problem:
# # Given username and password:
# username = "Saurabh"
# password = "12345"
# real_username = "Saurabh"
# real_password = "12345"

# # If username is correct:
# if username == real_username:
#     # Check password
#     if password == real_password:
#         print("Login successful")
#     else:
#         print("Invalid password")
# else:
#     print("Invalid username ")
# Problem:



# 8️⃣ Discount Calculator
# Concepts: nested if–elif, conditions inside conditions
# Problem:
# Given amount and is_member:

# amount = 10000
# is_member = True
# If member:
# if is_member:
# # 20% discount if amount ≥ 1000
#     if amount >= 1000:
#         print("your got 20% discount.")
#         print(f"The final price is {amount -  amount*(20/100)}")
# # 10% otherwise
#     else:
#         print("you got 10% discount")
#         print(f"The final price is {amount -  amount*(10/100)}")
# else:
#     if amount >= 2000:
#         print("you got 5% discount")
#         print(f"The final price is {amount -  amount*(5/100)}")

#     else:
#         print("you have't got any discount.")



# If not member:

# 5% discount if amount ≥ 2000

# No discount otherwise

# Print final price.


# 🔴 Level 5 — Advanced & Edge Cases
# 9️⃣ Triangle Type Checker
# Concepts: validity check + multiple conditions
# Problem:
# # Given sides a, b, c:
# a = 7
# b = 7
# c = 10

# if (a+b) > c and (a+c) > b and (b+c) > a:
# # First check if triangle is valid

# # Then print:

# # "Equilateral"
#     if a == b == c:
#         print("The given triangle is equilateral tiangle.")
# # "Isosceles"
#     elif (a == b != c) or (b == c != a) or (a == c != b):
#         print("The given tirangle is Isosceles.")
# # "Scalene"
#     else:
#         print("This is a scalene tirangle")
# else:
#     print("Invalid Triangle")

# 🔟 Number Classifier (Interview-Level)

# Concepts covered:
# ✅ comparisons
# ✅ logical operators
# ✅ nesting
# ✅ multiple elif
# ✅ ordering logic

# Problem:
# Given a number x, print:
x = 10
if x < 0:
# "Negative"
    print("Negative")
elif x == 0:
# "Zero"
    print("Zero")
# "Small Positive" (1–10)
elif x >= 0 and x <= 10:
    print("Small Positive")
# "Medium Positive" (11–100)
elif x >= 11 and x <= 100:
    print("Medium Positive")
# "Large Positive" (>100)
else:
    print("Large Positive")