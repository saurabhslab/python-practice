# 🟢 Level 1 — Basics of Class & Object
# 1️⃣ Create a Simple Class & Object
# Concepts: class, object, attributes
# Problem:
# Create a class Car with attributes:
# brand
# color
# Create an object and print the values.
# class Car:
#     def __init__(self, brand, color):
#         self.brand = brand
#         self.color = color
#     def display_values(self):
#         print(f"Car brand: {self.brand}, Car color: {self.color}")

# car1 = Car(brand = "Tesla", color = "Black")
# car1.display_values()
        


# 2️⃣ Add Methods to a Class
# Concepts: instance methods
# Problem:
# Create a class Student with:
# attributes: name, marks
# method: display() → prints name and marks.
# Create 2 objects and call the method.
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def display(self):
#         print(f"Name: {self.name}\nMarks: {self.marks}")


# student_fudan = Student("Fudan", 56)
# student_fudan.display()


# 🟡 Level 2 — Constructors & Instance Variables
# 3️⃣ Use __init__ Constructor
# Concepts: constructor, instance variables
# Problem:
# Create class Rectangle with:
# length, width
# method area() → return area
# method perimeter() → return perimeters
# Make 2 rectangles and print area of each.
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        pass
    def area(self):
        area_rectangle = self.length * self.width
        return area_rectangle
    def perimeter(self):
        return self.length, self.width
    
R1 = Rectangle(43, 23)
R2 = Rectangle(100, 20)

print(R1.area())
print(R2.area())

# 4️⃣ Modify Attribute Values Through Methods

# Concepts: setters (not private yet)
# Problem:
# Class BankAccount:

# attributes: owner, balance

# method: deposit(amount)

# method: withdraw(amount)

# Create an object and test both functions.

# 🟠 Level 3 — Class Variables & Static Methods
# 5️⃣ Class Variable + Instance Counter

# Concepts: class variable, counting objects
# Problem:
# Create class Employee:

# instance vars: name, salary

# class var: count → total employees

# increment count in constructor

# method to display employee info

# class method to show total count

# 6️⃣ Static Method for Utility Function

# Concepts: @staticmethod
# Problem:
# Create MathHelper class:

# static method: is_even(n)

# static method: square(n)

# Call without creating object.

# 🔵 Level 4 — Encapsulation & Properties
# 7️⃣ Encapsulation Using Private Variables

# Concepts: private variable __balance, getter, setter
# Problem:
# Class Wallet:

# private attribute __money

# add(amount)

# spend(amount) → spend only if enough

# getter: get_balance()

# Try accessing private variable directly → should fail.

# 8️⃣ Properties (@property)

# Concepts: property, setter
# Problem:
# Class Temperature:

# private attribute __celsius

# property celsius

# setter validates: cannot go below absolute zero (-273.15)

# Create object and test.

# 🔴 Level 5 — Inheritance, Polymorphism, Magic Methods, Composition
# 9️⃣ Inheritance + Method Overriding

# Concepts: inheritance, polymorphism
# Problem:
# Create:

# Class Animal:

# method sound()

# Class Dog(Animal)

# override: sound → "Bark"

# Class Cat(Animal)

# sound → "Meow"

# Loop over objects and call sound().

# 🔟 Build a Real Project Using Multiple Concepts

# Concepts:
# composition, class interaction, magic method __str__, object list management

# Problem:
# Create a system:

# Class Book:

# title

# author

# price

# __str__() → nicely print book details

# Class Library:

# attribute: books (list)

# methods:

# add_book(book)

# remove_book(title)

# find_book(title)

# display_all_books()

# Create few books, add to library, search and remove.