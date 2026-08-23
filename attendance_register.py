# --------------------------------------------
# Student Attendance Register
# VESA Skill Development Program - Project 2
# Domain: Python Programming
# --------------------------------------------

print("=" * 50)
print("        STUDENT ATTENDANCE REGISTER")
print("=" * 50)

print("Welcome to the Attendance Management System!")

# Dictionary to store all student records
students = {}


# Function to add a new student
def add_student():
    roll_number = input("Enter Roll Number: ").strip()

    # Check whether the roll number already exists
    if roll_number in students:
        print("Error: This Roll Number is already registered.")
        return

    name = input("Enter Student Name: ").strip()

    students[roll_number] = {
        "name": name,
        "attendance": []
    }

    print(f"\nStudent {name} added successfully.")


# Function to display all registered students
def display_students():
    if not students:
        print("\nNo students have been registered yet.")
        return

    print("\n" + "=" * 50)
    print("              STUDENT LIST")
    print("=" * 50)

    for roll_number, student in students.items():
        print(f"Roll Number : {roll_number}")
        print(f"Name        : {student['name']}")
        print("-" * 50)


# Function to search for a student using Roll Number
def search_student():
    roll_number = input("\nEnter Roll Number to search: ").strip()

    if roll_number in students:
        student = students[roll_number]

        print("\n" + "=" * 50)
        print("             STUDENT DETAILS")
        print("=" * 50)
        print(f"Roll Number : {roll_number}")
        print(f"Name        : {student['name']}")
        print(f"Attendance Records : {len(student['attendance'])}")
        print("=" * 50)
    else:
        print("\nStudent not found.")
        print("Please check the Roll Number and try again.")


# Add a student
print("\n--- Add Student ---")
add_student()

# Display all students
display_students()

# Search for a student
search_student()