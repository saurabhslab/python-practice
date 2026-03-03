"""1. Class & Object Basics
Create a class Car with:
attributes: brand, model, year
method: display_info() that prints all details
Create two objects and call the method.

class Class:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

car_1 = Class("Tesla", "Model S", 2021)
car_2 = Class("Mahindra", "Scorpio N", 2023)

car_1.display_info()
car_2.display_info() 
"""
# ________

"""2. Instance vs Class Variables
Create a class Student:
class variable: school_name
instance variables: name, roll_no
Print both instance and class variables for multiple students.

class Student:
    school_name = "Indian Public School"
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

student_1 = Student("Saurabh", 1)

print(student_1.name)
print(student_1.roll_no)
print(Student.school_name)"""


# ______
"""4. Simple Method Logic
Create a class BankAccount:
attributes: account_holder, balance
methods: deposit(amount), withdraw(amount)
Prevent withdrawal if balance is insufficient.

class BankAccount:
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.balance = balance 

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("The balance is insufficient")
        self.balance -= amount

person_1 = BankAccount("Saurabh Kumar", 1000000)

person_1.deposit(90)

print(person_1.balance)

person_1.withdraw(91)

print(person_1.balance)
"""
# ––––––--------
"""5. Encapsulation (Private Variables)
Create a class Employee:
private variable: __salary
methods: get_salary(), set_salary(amount)
Try accessing __salary directly and observe what happens."""

"""
class Employee:
    def __init__(self, salary):
        # Private variable
        self.__salary = salary

    # Getter method
    def get_salary(self):
        return self.__salary

    # Setter method
    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary amount")

# Create an Employee object
emp = Employee(50000)

# Accessing via getter
print("Salary (via getter):", emp.get_salary())

# Updating via setter
emp.set_salary(60000)
print("Updated Salary (via getter):", emp.get_salary())

# Trying to access directly
print(emp.__salary)   # ❌ This will raise an AttributeError

"""



# ––––––––––––––––--------------
"""Inheritance Basics
Create:
class Animal with method speak()
subclasses Dog and Cat that override speak()"""



 