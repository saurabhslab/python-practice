# 🟢 Level 1 — Basics
# 1️⃣ Print numbers from 1 to 10 (for loop)
# Task: Use a for loop with range() to print numbers 1–10.
# for i in range(1, 11):
#     print(i)

# 2️⃣ Print even numbers from 2 to 20 (while loop)
# Task: Start from 2 and keep adding 2 until 20. Use while.
# n = 2
# while n < 21:
#     print(n)
#     n += 2


# 🟡 Level 2 — Iterating collections
# 3️⃣ Sum of list values (for loop)
# list: [4, 7, 1, 3]
# Task: Use a for loop to compute the sum manually (no sum()).
# list = [4, 7, 1, 3]
# sum = 0
# for num in list:
#     sum += num

# print(sum)

# 4️⃣ Count vowels in a string
# string: "Programming"
# Task: Use a for loop, check vowels, count them.

# string = "Programming"
# count = 0
# for letter in string:
#     if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
#         count += 1

# print(count)



# 🟠 Level 3 — break, continue, loop/else

# 5️⃣ Find the first number divisible by 7 (break)
# Loop through numbers 1 to 100.
# Stop the loop when you find a number divisible by 7 and print it.
# for i in range(1, 101):
#     if i % 7 == 0:
#         print(i)
        #   break



# 6️⃣ Check if a number is prime (for–else)
# For a number n = 29:
# n = 29
# # Use for to check divisors
# def isprime(n):
#     if n <=1:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# print(isprime(n))
# If no divisor found → print "Prime"

# Use loop else to print result


# 🔵 Level 4 — Nested loops, patterns, iteration logic
# 7️⃣ Print a square pattern (nested for loop)
# For n = 4, print:
# ****
# ****
# ****
# ****

# for i in range(4):
#     for j in range(4):
#         print("*", end=" ")
#     print()   # moves to the next line
        
        

# 8️⃣ Multiplication table (nested loop)
# Print multiplication table from 1 to 10, like:
# 1 x 1 = 1
# 1 x 2 = 2
# ...
# # 10 x 10 = 100
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{j:2} x {i:2} = {i*j:3}", end="   ")  # fixed spacing
#     print()


# 🟣 Level 5 — While loops + logic + accumulators
# 9️⃣ Reverse a number using while
# Use a while loop to build reversed number → 54321.
# n = 12345
# reversed_no = 0

# while n > 0:
#     digit = n % 10              # get last digit
#     reversed_no = reversed_no * 10 + digit  # build reversed number
#     n = n // 10                 # remove last digit

# print(reversed_no)
    

# 🔟 Repeated user input until correct (while True + break)
# Simulate:
# Enter password: 
# Keep asking until user enters "python123", then print "Access granted".
simulate = "python123"
while True:
    user_input = input("Enter the password: ")
    if user_input == simulate:
        print("Access granted")
        break

