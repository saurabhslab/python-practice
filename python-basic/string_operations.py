# 🟢 Level 1 — Absolute Basics

# 1️⃣ Length, Indexing, Slicing
# Concepts: len(), indexing, slicing
# s = "Python"

# Tasks:
# Print the length of the string
# print(len(s))
# Print first and last character
# print(f"first character: {s[0]}, Last Character: {s[-1]}")
# Print "yth" using slicing
# print(s[1:4])


# 🟢 Level 2 — Case & Whitespace Handling
# 2️⃣ Case Conversion
# Concepts: upper(), lower(), title(), swapcase()
# s = "pYtHoN proGrAmMiNg"
# Tasks:
# Convert to all lowercase
# print(s.lower())
# Convert to title case
# print(s.title())
# Swap the case of each character
# print(s.swapcase())

# 3️⃣ Removing Extra Spaces
# Concepts: strip(), lstrip(), rstrip()
# s = "   hello world   "
# Tasks:
# Remove leading spaces only
# print(s.rstrip())
# Remove trailing spaces only
# print(s.lstrip())
# Remove both
# print(s.strip())


# 🟡 Level 3 — Search & Check

# 4️⃣ Find & Count
# Concepts: find(), count(), in
# s = "banana"
# Tasks:
# Find index of first "a"
# print(s.find("a"))
# Count how many times "a" appears
# print(s.count("a"))
# Check if "nan" exists in the string
# if "nan" in s:
#     print("yes 'nan' exists in the string.")
# else:
#     print("'nan' doesn't exists.")


# 5️⃣ String Checking Methods
# Concepts: isalpha(), isdigit(), isalnum(), isspace()

# values = ["Python3", "12345", "hello", "   "]
# Task:
# For each value, print which checks return True
# return_list = list(a.isalpha() for a in values)
# print(return_list)
# return_list = list(a.isdigit() for a in values)
# print(return_list)
# return_list = list(a.isalnum() for a in values)
# print(return_list)
# return_list = list(a.isspace() for a in values)
# print(return_list)


# 🟡 Level 4 — Replace & Split

# 6️⃣ Replace & Modify
# Concepts: replace()

# s = "I love Java. Java is powerful."
# Tasks:
# Replace "Java" with "Python"
# print(s.replace("Java", "Python"))
# Replace only the first occurrence
# print(s.replace("Java", "Python", 1))

# 7️⃣ Split & Join

# Concepts: split(), join()

# s = "Data Science with Python"
# Tasks:
# Split the string into words
# words_list = s.split(" ")
# print(words_list)
# Join words using "-"
# print("_".join(words_list))
# Reverse the order of words and join with space
# reversed_words_list = words_list[ : : -1]
# print(reversed_words_list)
# join_reversed_list = " ".join(reversed_words_list)
# print(join_reversed_list)

# 🔵 Level 5 — Formatting & Comparison

# 8️⃣ String Formatting
# Concepts: f-strings, format()
# name = "Saurabh"
# score = 92.4567
# Tasks:
# Print: Hello Saurabh, your score is 92.46
# Limit score to 2 decimal places
# print(f"Hello {name}, your score is {round(score, 2)}")


# 🔴 Level 6 — Logic + Real-World Thinking

# 🔟 String Analysis (Most Important)

# Concepts Covered:
# iteration, conditions, immutability, counting, methods
s = "Python is amazing!!! 123"
# Tasks:
# Count number of:
# alphabets


# digits

# spaces

# special characters

# Convert result into a formatted string summary

# ✅ Example Output:

# Alphabets: 15
# Digits: 3
# Spaces: 2
# Special Characters: 3

s = "Python is amazing!!! 123"

# Initialize counters
alphabets = digits = spaces = specials = 0

# Iterate through each character
for ch in s:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch.isspace():
        spaces += 1
    else:
        specials += 1

# Formatted summary using f-string
summary = (
    f"Summary:\n"
    f"Alphabets: {alphabets}\n"
    f"Digits: {digits}\n"
    f"Spaces: {spaces}\n"
    f"Special Characters: {specials}"
)

print(summary)