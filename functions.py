
"""
Student Record Management System
Codomax Digital - Module 02
"""

import csv
from pathlib import Path

FILE = Path(__file__).with_name("students.csv")

FIELDS = ["id", "name", "department", "marks"]


def read_students():
    if not FILE.exists():
        return []

    with open(FILE, "r", newline="") as file:
        return list(csv.DictReader(file))


def save_students(students):
    with open(FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(students)


# CREATE
def add_student():
    students = read_students()

    student_id = input("Enter Student ID: ")

    if any(s["id"] == student_id for s in students):
        print("Student ID already exists.")
        return

    name = input("Enter Student Name: ")
    department = input("Enter Department: ")
    marks = float(input("Enter Marks: "))

    if not 0 <= marks <= 100:
        print("Marks must be between 0 and 100.")
        return

    students.append({
        "id": student_id,
        "name": name,
        "department": department,
        "marks": str(marks)
    })

    save_students(students)
    print("Student Added Successfully!")


# READ
def view_students():
    students = read_students()

    if not students:
        print("No Student Records Found.")
        return

    for student in students:
        print(student)


# UPDATE
def update_student():
    students = read_students()

    student_id = input("Enter Student ID to Update: ")

    for student in students:
        if student["id"] == student_id:

            student["name"] = input("Enter New Name: ")
            student["department"] = input("Enter New Department: ")

            marks = float(input("Enter New Marks: "))

            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
                return

            student["marks"] = str(marks)

            save_students(students)
            print("Student Updated Successfully!")
            return

    print("Student Not Found!")


# DELETE
def delete_student():
    students = read_students()

    student_id = input("Enter Student ID to Delete: ")

    updated_students = [
        student for student in students
        if student["id"] != student_id
    ]

    if len(updated_students) == len(students):
        print("Student Not Found!")
        return

    save_students(updated_students)
    print("Student Deleted Successfully!")
