# # 🟢 Level 1: Absolute Basics

# # 1️⃣ Convert String to Integer
# # x = "25"
# # Task: Convert x to an integer and print type and value.
# # new_value = int(x)
# # print(new_value)
# # print(type(new_value))


# # 2️⃣ Convert Integer to Float
# # a = 10
# # Task: Convert a to float and print the result.

# # result = float(a)
# # print(result)



# # 🟡 Level 2: Simple Mixed Types

# # 3️⃣ Add Number and String
# # a = 5
# # b = "10"

# # Task: Add them correctly so output is 15.

# # result = a + int(b)
# # print(result)

# # 4️⃣ Convert Float to Integer
# x = 7.9
# # Task: Convert x to integer and explain the result.
# # result = int(x)
# # print(result)
# # decimal part truncated.


# 🟠 Level 3: Collections & Casting
# 5️⃣ String to List
# s = "python"
# Task: Convert s into a list.
# list_s = list(s)
# print(list_s)


# 6️⃣ List to Tuple and Set
# lst = [1, 2, 2, 3, 3, 4]
# Task:
# Convert to tuple
# tuple_lst = tuple(lst)
# print(tuple_lst)
# Convert to set
# set_lst = set(lst)
# print(set_lst)
# Explain the difference in output.



# 🔵 Level 4: Tricky & Real-World
# 7️⃣ Boolean Casting
# values = [0, 1, "", " ", [], [1], None]
# Task:
# Convert each element to bool and observe patterns.
# values_bool = [bool(v) for v in values]
# print(values_bool)

# 8️⃣ Input → Proper Types
# age = input("Enter your age: ")
# Task:
# Convert input so this works:
# age = int(age)
# print(age + 5)

# 🔴 Level 5: Advanced / Error-Prone
# 9️⃣ Invalid Casting Handling
# x = "12.5"
# Convert to float ✅
# f = float(x)
# print("Float:", f)   # 12.5

# Convert to int ❌ (safe handling)
# try:
    # i = int(x)   # This will raise ValueError
#     print("Int:", i)
# except ValueError:
#     print("Int conversion failed safely")


# 🔟 Nested Type Casting (Very Important)
data = "100,200,300"
# Task:
# Convert this into a list of integers:

data_str = list(data.split(","))
list_int = list(int(i) for i in data_str)
list_int_type = list(type(t) for t in list_int)
print(list_int)
print(list_int_type)

# [100, 200, 300]
