Day_08_File_Handling/file_handling.py
"""
Codomax Digital - Module 02
Day 08: File Handling, CSV and JSON
"""

import csv
import json

# 1. Writing a Text File
with open("student.txt", "w") as file:
    file.write("Name: Sadaquat\n")
    file.write("Department: Data Science\n")

# 2. Reading a Text File
with open("student.txt", "r") as file:
    print("Text File Information:")
    print(file.read())


# 3. Writing CSV File
students = [
    ["Name", "Department", "Marks"],
    ["Sadaquat", "Data Science", 85],
    ["Ali", "IT", 90],
    ["Ahmed", "Computer Science", 78]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(students)


# 4. Reading CSV File
print("\nCSV Records:")

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# 5. Writing JSON File
student = {
    "name": "Sadaquat",
    "department": "Data Science",
    "marks": 85
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)


# 6. Reading JSON File
with open("student.json", "r") as file:
    data = json.load(file)

print("\nJSON Information:")
print(data)
