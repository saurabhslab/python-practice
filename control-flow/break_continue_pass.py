# ✅ 10 Practice Problems — Break, Continue, Pass

# 🔹 Level 1 — Very Easy
# 1️⃣ Print numbers until 5 (break)
# Print numbers from 1 to 10, but stop printing when the number becomes 5 using break.
# n = 1
# while True:
#     print(n)
#     n +=1
#     if n ==6:
#         break

# 2️⃣ Skip printing even numbers (continue)
# Print numbers from 1 to 10, but skip all even numbers using continue.
# for i in range(1, 10):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i)

# 3️⃣ Use pass inside a loop
# Write a loop from 1 to 5.
# If the number is 3, do nothing using pass. Print numbers normally.
# for i in range(1, 5):
#     if i == 3:
#         continue
#     print(i)


# 🔹 Level 2 — Easy
# 4️⃣ Find first negative number (break)
# Loop over it and stop when you find the first negative number. Print that negative number.
# Given a list:
# nums = [10, 20, 5, -3, 7, -1]
# for num in nums:
#     if num < 0:
#         print(num)
#         break

# 5️⃣ Count only positive numbers (continue)
# Given:
# nums = [3, -2, 7, -9, 11, -4]
# Print only the positive numbers using continue.
# for num in nums:
#     if num <= 0:
#         continue
#     else:
#         print(num)

# 6️⃣ Find word starting with target letter (break)
# Words:
# words = ["cat", "dog", "cow", "deer", "camel"]
# Take user input letter and find the first word starting with that letter.
# Stop searching using break.
# user_input = input("Enter the letter: ")
# for word in words:
#     if user_input == word[0]:
#         print(word)
#         break


# 🔹 Level 3 — Moderate
# 7️⃣ Loop inside loop + break outer loop
# Print a multiplication table 1–10,
# but stop everything completely when the product becomes 50.
# (Hint: break only stops inner loop — you must handle outer loop yourself.)
# for i in range(1, 11):
#     for j in range(1, 11):
#         if i * j == 50:
#             break
#         else:
#             print(f"{i} x {j} = {i*j}", end = " ")
#         print()
#     print()

# 8️⃣ Skip all vowels in a string (continue)
# Input: "Python Programming"
# Print the string but skip vowels using continue.
# required_string = ""
# string_input = "Python Programming"
# for ch in string_input:
#     if ch in "aeiou":
#         continue
#     else:
#         required_string += ch
# print(required_string)

# 9️⃣ Placeholder using pass
# Define a function:
# def future_feature():
# Inside it, correctly use pass so the code does not error.
    # do nothing
# Call the function to confirm it works.
    # pass
# future_feature()


# 🔹 Level 4 — Tricky / Advanced
# 🔟 Find prime numbers up to N using break inside inner loop
# Write a program to print all primes from 2 to N.
# Use:
# break to stop checking divisibility early
# continue where necessary
# Avoid unnecessary checks
# Example: For N = 20 → output primes.


N = 20

for num in range(2, N+1):          # check numbers from 2 to N
    is_prime = True

    # only check divisors up to sqrt(num)
    for div in range(2, int(num**0.5) + 1):
        if num % div == 0:         # found a divisor
            is_prime = False
            break                  # stop checking further
    if not is_prime:
        continue                   # skip non-primes

    print(num, end=" ")            # print prime


