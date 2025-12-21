# ✅ 10 Practice Problems on Decorators (Beginner → Advanced)
# 1️⃣ Basic Decorator — Print Before & After
# Concepts: Basic decorator structure
# Task:
# Create a decorator announce that prints "Starting..." before a function runs and "Done!" after it runs.
# Use it on a function greet() that prints "Hello".


# def decorator(func):
    
#     def wrapper():
#         print("Starting")
#         func()
#         print("Done")
        
#     return wrapper

# @decorator
# def greet():
#     print("Hellow Saurabh!")

# greet()

# 2️⃣ Decorator That Returns Modified Valuef
# Concepts: Returning values from decorated functions
# Task:
# Create a decorator double_output that doubles the return value of any function it wraps.
# Apply it to a function that returns 5 → output should become 10.
# def double_output(func):
#     def wrapper(*arg, **kwrags):
#         result = func(*arg, **kwrags)
#         return result * 2
#     return wrapper

# @double_output   
# def add(a, b):
#     return a + b

# print(add(3, 2))

# 3️⃣ Decorator That Logs Function Name
# Concepts: func.__name__, wrapper basics
# Task:
# Create a decorator log_name that prints:
# "You called <function_name>"
# every time the function is executed.

def log_name(func):
    def wrapper(*args, **kwargs):
        func()
        result = func.__name__
        return f"you called {result}"
    return wrapper

@log_name
def example():
    return "This is the name of the function"

print(example())
# **4️⃣ Decorator That Works With *args and kwargs


# Concepts: Argument forwarding
# Task:
# Create a decorator debug that prints all positional and keyword arguments passed to the function.

# Example:
# add(4, 5, x=10)
# should print the args & kwargs.

# 5️⃣ Decorator That Measures Execution Time

# Concepts: time.time(), practical decorators
# Task:
# Write a decorator timer that prints how long the function took to execute.

# Use it on a function that loops from 1 to 1,000,000.

# 6️⃣ Decorator With Its Own Arguments

# Concepts: Decorators returning decorators
# Task:
# Create a decorator repeat(n) that runs the decorated function n times.

# Example:

# @repeat(3)
# def hello():
#     print("Hi")


# Output:
# Hi
# Hi
# Hi

# 7️⃣ Stateful Decorator — Count Function Calls

# Concepts: Closures, maintaining state
# Task:
# Create a decorator counter that counts how many times a function is called.
# Each time the function runs, print:

# "Call number: X"

# 8️⃣ Apply Multiple Decorators (Chaining)

# Concepts: Order of decorators
# Task:
# Create two decorators:

# bold → wraps text in <b>...</b>

# italic → wraps text in <i>...</i>

# Apply them like:

# @bold
# @italic
# def message():
#     return "Hello"


# Print output.
# Also observe how the order changes the result.

# 9️⃣ Class-Based Decorator

# Concepts: __call__, storing state in classes
# Task:
# Create a class decorator Track that counts how many times the function is called.

# Example:

# @Track
# def greet():
#     print("Hi")


# greet() → prints call number each time.

# 🔟 Real-World Use Case — Authentication Decorator

# Concepts: Conditional execution
# Task:
# Write a decorator require_login that only runs the function if:

# user = {"logged_in": True}


# If False, print "Access Denied".