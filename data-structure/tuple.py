# ✅ 10 Practice Problems on Tuples (Beginner → Advanced)

# 1️⃣ Create a Tuple (Basics) — Very Easy
# Problem:
# Create a tuple colors with values "red", "green", "blue" and print it.
# Concepts: tuple creation, basics.
# tpl = ("red", "green", "Yelllow")
# print(type(tpl))

# 2️⃣ Access Elements Using Indexing
# Problem:
# Given:
# nums = (10, 20, 30, 40, 50)
# Print:
# First element
# print(nums[0])
# Last element
# print(nums[-1])
# Second element
# print(nums[1])
# Concept: indexing.

# 3️⃣ Slicing a Tuple
# Problem:
# Given:
# t = (1, 2, 3, 4, 5, 6, 7)
# Print:
# (3, 4, 5) using slicing
# print(t[2:5])
# Last three items using slicing
# print(t[-3:])
# Concept: slicing.

# 4️⃣ Tuple Unpacking
# Problem:
# Given:
# point = (4, 7)
# Unpack it into variables x and y and print them.
# x, y = point
# print(x, y)
# Concept: unpacking.

# 5️⃣ Extended Tuple Unpacking
# Problem:
# Given:
# data = (10, 20, 30, 40, 50)
# Unpack so that:
# a = 10
# b = 20
# others = (30, 40, 50)
# a, b, *others = data
# print(a, b, others)
# Use * operator.

# 6️⃣ Immutability Test (Important)
# Problem:
# Given:
# t = (1, 2, 3)
# Try to do:
# t[1] = 5
# Observe and print what error occurs.
# tuple object is immutable meaning we can't modify the original
# Concept: tuples cannot be changed (immutable).

# 7️⃣ Nested Tuple Access
# Problem:
# Given:
# student = ("Saurabh", (90, 85, 92))
# Print:
# "Saurabh"
# print(student[0])
# The second score (85)
# print(student[1][1])

# 8️⃣ Tuple Methods
# Problem:
# Given:
# t = (1, 2, 2, 3, 2, 4)
# Use tuple methods to print:
# How many times 2 appears
# print(t.count(2))
# Index of first occurrence of 3
# print(t.index(3))
# Concept: .count(), .index().

# 9️⃣ Convert Between Tuple & List
# Problem:
# Given:
# t = (1, 2, 3, 4)
# Convert the tuple to a list → modify list by adding 5 → convert back to tuple.
# lst = list(t)
# lst.append(5)
# print(lst)
# tpl = tuple(lst)
# Print final tuple.
# print(tpl)
# Concept: mutability workaround, conversions.

# 🔟 Tuple as Dictionary Key (Advanced & Important)
# Problem:
# You cannot use lists as dict keys, but tuples work.
# Create a dictionary:
locations = {}
# Now store:
locations[(10.2, 20.5)] = "Your Home"
locations[(15.5, 30.1)] = "Office"
# Then print all key–value pairs.
print(locations)
# Concept: tuples are hashable → can be dict keys.