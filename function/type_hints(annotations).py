# Level 1: The Fundamentals
# Focus: Basic types and function signatures.

# 1. Basic Function Hints Annotate a function called calculate_area that takes a radius (float) and returns the area (float).
# Goal: Master int, float, str, and bool.
# import math
# def calculate_area(radius: float) -> float:
#     math.pi * radius ** 2

# 2. List and Dictionary Basics 
# Annotate a function get_usernames that takes a list of integers (user IDs) and returns a list of strings (usernames).
# Goal: Use list[int] and list[str] (Python 3.9+) or List from the typing module.
# def get_usernames(user_ids: list[int]) -> list[str]:
#      return [f"user_{uid}" for uid in user_ids]
    
# 3. Optional Values Create a function format_greeting that takes a name (string) and an optional title (string). If title is not provided, it defaults to None.

def format_greeting(name: str, title: str | None = None) -> str:
    # return f"Hello {title} {name}" if title else f"Hello {name}"

# Goal: Use Optional[str] or str | None.

# Level 2: Advanced Containers & Logic
# Focus: Structured data and flexible types.

# 4. Complex Dictionaries Annotate a function process_scores that accepts a dictionary where keys are strings (student names) and values are lists of integers (test scores).

# Goal: Use dict[str, list[int]].

# 5. Multiple Return Types (Unions) Annotate a function parse_input that takes a string. If the string is numeric, return an int; otherwise, return the original str.

# Goal: Use Union[int, str] or int | str.

# 6. Type Aliases Define a type alias called Point which is a tuple of two floats. Then, annotate a function distance that takes two Point objects and returns a float.

# Goal: Improve readability by naming complex types.

# Level 3: Classes and Callables
# Focus: Object-oriented programming and functional logic.

# 7. Class Methods Create a class Product. Annotate the __init__ method (taking name and price) and a method get_discounted_price that takes a float and returns a float.

# Goal: Remember that __init__ always returns None.

# 8. Callback Functions Annotate a function apply_transformation that takes a list of integers and a callback. The callback should be a function that takes one integer and returns an integer.

# Goal: Use Callable[[int], int].

# Level 4: Generics and Constants
# Focus: Flexible yet strict definitions.

# 9. Generic Functions Annotate a function get_first_element that takes a list of "Any Type" and returns a single element of that same type.

# Goal: Use TypeVar to ensure the input and output types match.

# 10. Literal Types Annotate a function adjust_volume that takes a current volume (int) and a direction. The direction must be strictly either the string "UP" or the string "DOWN".

# Goal: Use Literal["UP", "DOWN"].

