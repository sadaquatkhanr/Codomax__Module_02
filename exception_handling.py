Day_09_Exception_Handling/exception_handling.py
"""
Codomax Digital - Module 02
Day 09: Exception Handling and Debugging
"""

try:
    student_name = input("Enter Student Name: ")

    mark1 = float(input("Enter First Subject Marks: "))
    mark2 = float(input("Enter Second Subject Marks: "))

    if not (0 <= mark1 <= 100 and 0 <= mark2 <= 100):
        raise ValueError("Marks must be between 0 and 100.")

    average = (mark1 + mark2) / 2

except ValueError as error:
    print("Invalid Input:", error)

else:
    print("\nStudent Name:", student_name)
    print("Average Marks:", average)

finally:
    print("Program Execution Completed.")
