# 🟢 Level 1: List Comprehensions
# 1. The Square Filter
# Given a list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], create a new list containing the squares of only the odd numbers.

"""no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = [x**2 for x in no if x % 2 != 0]
print(new_list)"""

# 2. String Lengths
# Given a list of names names = ["Alice", "Bob", "Christopher", "Dan"], create a list of integers representing the length of each name, but only if the name has more than 3 characters.

names = ["Alice", "Bob", "Christopher", "Dan"]
new_list = [len(name) for name in names if len(name)>3]
print(new_list)

# 3. Vowel Stripper
# Given a string text = "Hello World", create a list of all characters in the string that are not vowels (ignore case).



# 🟡 Level 2: Dictionary Comprehensions
# 4. Price Mapper
# Given a list of products products = ["Apple", "Banana", "Cherry"] and their prices prices = [1.2, 0.5, 2.5], create a dictionary where the product is the key and the price is the value.
# Hint: Use zip().

# 5. State Toggle
# Given a dictionary status = {"WiFi": "on", "Bluetooth": "off", "NFC": "on"}, create a new dictionary where each value is inverted (e.g., "on" becomes "off" and vice versa).

# 6. Frequency Map
# Given a string word = "abracadabra", create a dictionary where each key is a character and the value is the number of times it appears in the string.

# 🔴 Level 3: Nested & Complex Logic
# 7. Matrix Flattening
# Given a 2D list matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]], create a single flat list containing all the numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9].

# 8. Transpose a Matrix
# Using the same matrix from Problem 7, create a new 2D list that is the transpose (swap rows and columns).
# Result should be: [[1, 4, 7], [2, 5, 8], [3, 6, 9]].

# 9. Filtered Dictionary of Lists
# Given a dictionary scores = {"TeamA": [10, 20, 30], "TeamB": [5, 15], "TeamC": [40, 50, 60]}, create a new dictionary containing only the teams that have an average score greater than 20.

# 10. Conditional Key Transformation
# Given a list data = [1, "apple", 2, "banana", 3], create a dictionary where:

# If the item is a number, the key is the number and the value is its square.

# If the item is a string, the key is the string and the value is the string in uppercase.