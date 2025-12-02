# 🟢 Level 1 — Basics

# 1. Simple Assignment # Create a variable age with your age and print it.
# age = 25
# print(age)


# 2. Multiple Variables # Store your name, age, and city in three different variables and print them in one sentence.
# name = "Saurabh Kumar"
# age = 25
# city = "Begusarai"

# print("Name: ",name, "\nAge: ", age, "\nCity: ",city)





# 🟡 Level 2 — Understanding Types

# 3. Type Identification # Create variables of type:
# int
# float
# string
# boolean
# Print each variable and its type using type().

# var_int = 23
# var_float = 0.23
# var_string = "Saurabh Kumar"
# var_boolean = False

# print(type(var_int))
# print(type(var_float))
# print(type(var_string))
# print(type(var_boolean))


# 4. Variable Reassignment

# Assign x = 10.
# Change x to "Python" without creating a new variable.
# Print both values to observe behavior.

# x = 10
# print(x)
# x = "python"
# print(x)




# 🟠 Level 3 — Input & Conversion

# 5. User Input + Type Casting
# Take two numbers from the user as input and store them in variables.
# Print their sum (ensure correct numeric addition, not string concatenation).

# num1 = int(input("Enter the first no: "))
# num2 = int(input("Enter the second no: "))

# print(num1 + num2)



# 6. Swap Variables (No Temp Variable)
# Swap values of a = 5 and b = 10 without using a third variable.
# a = 5 
# b = 10
# a, b = b, a
# print(a, b)




# 🔵 Level 4 — Scope & Reference Behavior

# 7. Variable Scope
# Creat a variable x = 50 outside a function.
# Inside a function, try changing its value and observe the output.
# x = 50
# def variable_type():
#     x = 40
#     return x

# print(variable_type())

# Explain:
# Why does it change or not change?
# it gets globle varialbe when there is no local variable to access

# 8. Mutable vs Immutable Variables
# Create:
# a list variable
# an integer variable
# Modify both and observe:
# Which changes in-place?
# Which creates a new object?

# var_list = [23, "Saurabh Kumar", False]
# var_int = 23

# var_list = [23]
# var_int  = 35
# print(var_list, var_int)

# both modified




# 🔴 Level 5 — Advanced Variable Concepts

# 9. Reference Copy vs Deep Copy

# Create a list variable:

# a = [1, 2, 3]
# b = a
# b = 23

# Modify b and print both a and b.
# print(a, b)

# Then use proper copying to avoid this issue.

# b = a.copy()
# print(a, b)


# 10. Dynamic Variable Creation

# Write a program that:
# Takes a string from the user
# Uses it as a variable name
# Stores a number in it dynamically
# (Hint: use globals() or locals())

var_str = input("Enter a string: ")
var_str = 43
print(var_str)

