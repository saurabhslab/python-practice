# ✅ 10 Practice Problems on Lists (Beginner → Advanced)

# 🟢 1. Print First, Last & Middle Elements
# Concepts: indexing, len()
# Problem:
# Given a list:
# nums = [10, 20, 30, 40, 50]
# Print:
# First element
# print(nums[0])
# Last element
# print(nums[-1])
# Middle element
# print(nums[2])

# 🟢 2. Slice the List
# Concepts: slicing
# Problem:
# Given:
# letters = ['a', 'b', 'c', 'd', 'e', 'f']
# Print:
# First 3 elements
# print(letters[:3])
# Last 2 elements
# print(letters[-2:])
# Elements from index 2 to 4
# print(letters[2:4])

# 🟢 3. Replace Elements Using Indexing
# Concepts: mutability, assignment
# Problem:
# Given:
# a = [1, 2, 3, 4]
# Change the 2nd element to 99 and last element to 100.
# a[1] = 99
# a[-1] = 100
# print(a)

# 🟡 4. Add & Remove Elements
# Concepts: append(), insert(), pop(), remove()
# Problem:
# Start with:
# lst = [5, 10, 15]
# Perform:
# Append 20
# lst.append(20)
# Insert 99 at index 1
# lst.insert(2, 1000)
# Remove 10
# lst.remove(10)
# Pop the last element
# lst.pop()
# Print final list.
# print(lst)

# 🟡 5. Check if Element Exists
# Concepts: in operator, count()
# Problem:
# Given:
# items = [3, 7, 3, 9, 3, 2]
# Check if 9 is in the list
# if 9 in items:
#     print("True")
# Count how many times 3 appears
# count = 0
# for i in items:
#     if i == 3:
#         count += 1
# print(count)

# 🟡 6. Sum, Max, Min of List
# Concepts: built-in functions
# Problem:
# Given:
# data = [4, 1, 9, 12, 3]
# Print:
# Sum
# Maximum
# Minimum
# data_sum = sum(data)
# data_max = max(data)
# data_min = min(data)
# print(f"Sum of the no in list = {data_sum}\n Max no in list = {data_max}\n Min no in list = {data_min}")

# 🟠 7. Loop Through List & Modify Values
# Concepts: for-loop, updating values
# Problem:
# Given:
# nums = [1, 2, 3, 4]
# Create a new list where each number is multiplied by 10:
# new_list = []
# for num in nums:
    # new_list.append(num*10)
# print(new_list)
# [10, 20, 30, 40]

# 🟠 8. Flatten a Nested List (Easy Version)
# Concepts: nested lists, loops
# Problem:
# Given:
# lst = [[1, 2], [3, 4], [5, 6]]
# new_list = []
# for nested_lst in lst:
#     for num in nested_lst:
#         new_list.append(num)

# print(new_list)
# Output a flat list:
# [1, 2, 3, 4, 5, 6]

# 🔴 9. Deep Copy vs Shallow Copy Practice
# Concepts: copy(), deepcopy(), mutability
# Problem:
# # Given:
# a = [1, 2, [3, 4]]
# b = a.copy()
# b[2][0] = 99
# print(a)
# What is value of a?
# [1, 2, [99,4]]
# What is value of b?
# [1, 2,[99, 4]]
# Why does a change?
# outer list copied inner list shared

# 🔴 10. List Comprehension (With Condition)
# Concepts: filtering, transformation
# Problem:
# Given:
nums = [1, 2, 3, 4, 5, 6]
# Create a new list that contains squares of even numbers only:
# [4, 16, 36]
new_list = [x**2 for x in nums if x % 2 == 0]
print(new_list)