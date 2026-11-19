	Day_07_Lambda/lambda_comprehension.py
"""
Codomax Digital - Module 02
Day 07: Lambda Functions and List Comprehensions
"""

# 1. Lambda Addition
addition = lambda a, b: a + b
print("Addition:", addition(10, 5))


# 2. Lambda Multiplication
multiply = lambda a, b: a * b
print("Multiplication:", multiply(10, 5))


# 3. List of Numbers
numbers = list(range(1, 21))
print("Original Numbers:", numbers)


# 4. Squares using List Comprehension
squares = [number ** 2 for number in numbers]
print("Squares:", squares)


# 5. Even Numbers
even_numbers = [number for number in numbers if number % 2 == 0]
print("Even Numbers:", even_numbers)


# 6. Numbers Greater Than 50
marks = [20, 45, 55, 70, 30, 90]
greater_marks = [mark for mark in marks if mark > 50]

print("Marks Greater Than 50:", greater_marks)
