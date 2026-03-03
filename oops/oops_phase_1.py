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
# ---------------------  
class Circle: 
    pi = 3.14159
    def __init__(self,r):
        self.r = r
    

circle_1 = Circle(23)
circle_2 = Circle(34)

print(circle_1.r)
print(circle_2.r)


