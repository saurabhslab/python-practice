# Problem 1: Basic Inheritance
# Create a parent class Animal with a method speak() that prints "Animal makes a sound." Create a child class Dog that inherits from Animal. Create an instance of Dog and call the speak() method.


# Problem 2: Method Overriding
# Using the classes from Problem 1, override the speak() method in the Dog class so that it prints "Woof! Woof!" instead of the generic animal sound.

# Problem 3: The super() Keyword
# Create a class Employee with attributes name and salary. Create a child class Manager that inherits from Employee but adds a new attribute department. Use the super().__init__ method to initialize the name and salary from the parent class.

# Problem 4: Private Attributes (Encapsulation)
# Create a Smartphone class where the attribute __battery_level is private. Provide a method charge() that increases the battery and a method get_status() that prints the current battery level. Try to access __battery_level directly from outside the class to see the error.

# Problem 5: Protected Members
# Create a class Base with a protected attribute _database_url. Create a subclass DevBase that accesses and prints _database_url. While Python doesn't strictly enforce "protected" status, explain in a comment why we use the single underscore.

# Problem 6: Polymorphism with Methods
# Create two classes, Cat and Cow. Both should have a method named sound().

# Cat.sound() prints "Meow"

# Cow.sound() prints "Moo" Write a function called make_it_speak(animal) that takes an object as an argument and calls its .sound() method, regardless of whether it's a cat or a cow.

# Problem 7: Polymorphism in a Loop
# Create a list containing instances of Rectangle, Circle, and Triangle. Ensure each class has an area() method. Iterate through the list and print the area of each shape without checking what type of shape it is.

# Problem 8: Abstract Base Classes (Abstraction)
# Use the abc module to create an abstract class Vehicle. Define an abstract method start_engine(). Create a subclass Motorbike. Show what happens if you try to instantiate Vehicle directly, and then implement start_engine() in Motorbike to make it work.

# Problem 9: Multi-Level Inheritance
# Create a hierarchy: Vehicle -> Car -> ElectricCar.

# Vehicle has a method move().

# Car has a method refuel().

# ElectricCar overrides refuel() to say "Charging battery." Create an ElectricCar object and demonstrate that it has access to methods from all three levels.

# Problem 10: Encapsulation with Logic
# Create a CreditCard class with a private __limit. Create a method set_limit(amount). Inside this method, add logic: the limit can only be increased if the amount is positive and does not exceed $10,000. This is the essence of Encapsulation—protecting data from invalid changes.