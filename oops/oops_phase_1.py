# Problem 1: The Blueprint
# Create a class named Laptop. Define an empty class using the pass keyword. Instantiate two different objects from this class and print their memory addresses to prove they are unique.

# class Laptop:
#     pass

# object_1 = Laptop()
# object_2 = Laptop()

# print(id(object_1))
# print(id(object_2))


# Problem 2: The Constructor
# Create a Book class. Use the __init__methd to initialize three attributes: title, author, and price. Create an instance of a book (e.g., "The Great Gatsby") and print its author.

# class Book: 
#     def __init__(self, title: str, author: str, price: int):
#         self.title = title
#         self.autor = author
#         self.price = price

# B_1 = Book("The Great Gatsby", "Tom Cruise", "100")

# print(B_1.autor)

# Problem 3: The "Self" Talk
# Create a User class with a username. Add a method called greet that prints "Hello, my name is [username]!".

# class User:
#     def __init__(self, username: str):
#         self.username = username
    
#     def greet(self):
#         print(f"Hello, my name is {self.username}.")

# user_1 = User("Saurabh")

# user_1.greet()

# Challenge: Ensure you use self.username inside the method so it accesses the specific instance's data.

# Problem 4: Class vs. Instance Attributes
# Create a Circle class.

# Define a class attribute pi = 3.14159.

# Define an instance attribute radius via __init__.

# Create two circles with different radii and show that they both can access the same pi value.

# Problem 5: The Modifier
# Create a Smartphone class with brand and battery_level (defaulting to 100). Add a method use_app(amount) that subtracts the amount from the battery_level. Print the battery level before and after using an app.

# Problem 6: Counting Instances
# Create a Robot class. Add a class attribute population set to 0. Every time a new Robot is created (in __init__), increment population by 1. Create three robots and print Robot.population.

# Problem 7: String Representation (Intro)
# Create a Car class with make and model. Inside the class, create a method called description that returns a formatted string like "This car is a 2023 Tesla".

# Problem 8: The Dynamic Attribute
# Create a Product class with name and price. Create an instance. After the instance is created, try adding a new attribute called discount directly to that specific object (e.g., item1.discount = 0.2). Print it to show that Python allows dynamic attribute assignment.

# Problem 9: Data Validation
# Create a BankAccount class with balance. In the __init__ method, add a check: if the starting balance is negative, set it to 0 and print a warning message. Test this by trying to create an account with -500 dollars.

# Problem 10: The Mini-System
# Create a Student class.

# Attributes: name, grades (a list).

# Method: add_grade(grade) to append a new grade to the list.

# Method: get_average() to return the mean of the grades.

# Task: Create "Alex," add grades 85, 90, and 78, then print their average.