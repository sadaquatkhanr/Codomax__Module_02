Day_10_Final_Project.
"""
Student Record Management System
Main Program
"""
from functions import (
    add_student,
    view_students,
    update_student,
    delete_student
)



while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")

    print("1. Add Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter Your Choice: ")

    try:

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            update_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            print("Thank You!")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please Enter Valid Information.")

    except OSError as error:
        print("File Error:", error)
