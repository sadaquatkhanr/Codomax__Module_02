Day_09_Exception_Handling/debugging_examples.md

## 1. Syntax Error

Incorrect:
```python
if 10 > 5
    print("Correct")
```

Correct:
```python
if 10 > 5:
    print("Correct")
```

## 2. Runtime Error

Incorrect:
```python
number = 10 / 0
```

Error: ZeroDivisionError

Correct:
```python
try:
    number = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
```

## 3. Logical Error

Incorrect:
```python
a = 10
b = 20
result = a - b
```

Correct:
```python
result = a + b
```

## Definition

Debugging is the process of identifying and correcting errors in a program.
