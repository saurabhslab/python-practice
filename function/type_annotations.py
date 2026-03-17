"""Practice Question 1
Create variables with type annotations:
user_id → integer
username → string
is_active → boolean
"""
# user_id: int = 2343
# username: str = "Saurabh"
# is_active: bool = True
# ______
"""Question 2
Create a function:
multiply(a, b)
Requirements:
a → int
b → int
return type → int"""

# def multiply(a: int, b: int) -> int: 
#     a*b
# ___

"""Question 3
Create a function:
greet(user)
Requirements:
user → string
return type → string"""
# def greet(user: str) -> str:
#     return f"Hellow, {user}"
# __

"""Level 2 — List Types
Question 4
Create a variable:
numbers
Requirements:
list of integers"""

number: list[int] = [23, 23, 323]

# __
"""Question 5
Create a variable:
names
Requirements:
list of strings"""
# name: list[str] = ["Saurabh", "Einstein", "Newton", "AI"]
# __

"""Question 6
Create a function:
total(numbers)
Requirements:
parameter → list of integers
return type → integer"""

# def total(number: list[int]) -> int:
#     return sum(number)

# --
"""Question 7
Create a variable:
user
Requirements:
dictionary with
name → str
age → int
city → str"""

# user: dict[str, str | int] = {
#     "name": "Saurabh",
#     "age": 25,
#     "city": "Patna"
# }
#---

"""Write a function:
get_name(user)
Requirements:
parameter → dictionary of string keys and string values
return type → string"""

# def get_name(user: dict[str, str]) -> str:
#     pass 

"""Question 9 + 10 
Create a TypedDict called:
User
Fields:
id → int
name → str
email → str

also create a user variable
"""
"""
from typing import TypedDict

class User(TypedDict):
    id: int
    name: str
    email: str

user: User = {
    "id": 1,
    "name": "Saurabh",
    "email": "saurabh@example.com"
}
"""

"""Question 11
Create a TypedDict called:
Product
Fields:
name → str
price → float
stock → int """

"""from typing import TypedDict

class Product(TypedDict):
    name: str
    price: float
    stock: int

product: Product = {
    "name": "Laptop",
    "price": 79999.99,
    "stock": 10
}"""

"""Question 12
Write a function:
increase_stock(product)
Requirements:
parameter → Product
increase stock by 1
return updated Product"""

"""def increase_stock(product: Product) -> Product:
    product["stock"] += 1
    return product"""

"""Question 13
Write a function:
apply_discount(product)
Requirements:
parameter → Product
decrease price by 10
return updated Product"""

"""def apply_discount(product: Product) -> Product:
    product['price'] -= 10
    return product"""

"""Question 14
Create a TypedDict called:
Order
Fields:
order_id → int
items → list[str]
total_price → float"""

"""from typing import TypedDict

class Order(TypedDict):
    order_id: int
    items: list[str]
    total_price: float"""

"""Question 16

Create a TypedDict called:

ChatState

Fields:

user_input → str
messages → list[str]
response → str"""

"""from typing import TypedDict

class ChatState(TypedDict):
    user_input: str
    messages: list[str]
    response: str

chat: ChatState = {
    "user_input": "Hello, how are you?",
    "messages": ["Hi!", "I'm good, thanks."],
    "response": "I'm doing well, how about you?"
}
"""


