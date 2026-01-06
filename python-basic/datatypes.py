# 1️⃣ Identify the Data Type
# Write code to print the data type of each:
# x = 10
# y = 10.5
# z = True
# name = "Python" 

# print(type(x))
# print(type(y))
# print(type(z))
# print(type(name))


# 2️⃣ Convert Data Types
# Convert the value "123" into an integer and multiply by 5.
# num_str = "123"

# result = int(num_str) * 5

# print(result)

# 3️⃣ Mutable vs Immutable
# a = "hello"
# b = a
# b = b + " world"
# print(a, b)

# 4️⃣ List Indexing Practice
# Given:
# nums = [10, 20, 30, 40, 50]

# Write code to print:
# The first element
# print(nums[0])
# The last element
# print(nums[-1])
# The middle element
# print(nums[2])

# 5️⃣ Tuple Unpacking
# Given:
# data = ("Alice", 25, "Developer")
# Unpack this into variables: name, age, job, and print them.

# first, second, third = data

# print(first)
# print(second)
# print(third)


# 6️⃣ Nested List Modify

# Given:
# info = [1, 2, [3, 4, 5], 6]

# Change the value 4 → 99, and print the final list.

# info[2][1] = 99

# print(info)


# 7️⃣ Set Operations

# Given two sets:
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# Print:
# Union
# print(A | B)
# Intersection
# print(A & B)
# Difference (A-B)
# print(A - B)
# Symmetric difference
# print(A^B)

# 8️⃣ Dictionary Manipulation
# # Given:
# student = {
#     "name": "Sam",
#     "marks": {"math": 85, "science": 92}
# }

# Tasks:
# Add a new subject "english": 88
# student["marks"] = {"english": 88}
# Update math marks to 90
# student["marks"]["math"] = 90
# Print all keys and values
# print(student)

# 9️⃣ Detect Data Type and Modify

# Given the dynamic input:

# value = eval(input("Enter something: "))
# Write code to detect whether input is:
# number (int/float)
# string
# list
# tuple
# set
# dict
# Then print:
# "You entered a <datatype>"

# print(f"You entered {type(value)}")

# 🔟 Complex Nested Structure
# Given:

data = {
    "users": [
        {"id": 1, "name": "John", "skills": ("Python", "SQL")},
        {"id": 2, "name": "Emma", "skills": ("Java", "AWS")}
    ]
}

# Task
# Print the name of the second user.
# Add "Docker" to the second user’s skill (convert tuple temporarily to list then back).
# Print final updated data.


skills_list = list(data["users"][1]["skills"]) 
skills_list.append("Docker")
data["users"][1]["skills"] = tuple(skills_list)
print(data["users"][1])

