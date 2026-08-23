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


# Function to mark attendance for a student
def mark_attendance():
    roll_number = input("\nEnter Roll Number: ").strip()

    # Check whether the student exists
    if roll_number not in students:
        print("Student not found.")
        return

    student = students[roll_number]

    print(f"\nStudent: {student['name']}")
    print("P - Present")
    print("A - Absent")

    status = input("Enter attendance status: ").strip().upper()

    # Validate attendance status
    if status == "P":
        student["attendance"].append("P")
        print("Attendance marked as Present.")

    elif status == "A":
        student["attendance"].append("A")
        print("Attendance marked as Absent.")

    else:
        print("Invalid attendance status.")
        print("Please enter P for Present or A for Absent.")


# Function to calculate attendance percentage
def calculate_percentage(attendance):
    total_classes = len(attendance)

    if total_classes == 0:
        return 0

    present_classes = attendance.count("P")

    percentage = (present_classes / total_classes) * 100

    return percentage


# Function to display attendance percentage
def display_attendance():
    roll_number = input("\nEnter Roll Number: ").strip()

    if roll_number not in students:
        print("Student not found.")
        return

    student = students[roll_number]
    attendance = student["attendance"]

    total_classes = len(attendance)
    present_classes = attendance.count("P")
    absent_classes = attendance.count("A")

    percentage = calculate_percentage(attendance)

    print("\n" + "=" * 50)
    print("           ATTENDANCE REPORT")
    print("=" * 50)

    print(f"Roll Number    : {roll_number}")
    print(f"Student Name   : {student['name']}")
    print(f"Total Classes  : {total_classes}")
    print(f"Present        : {present_classes}")
    print(f"Absent         : {absent_classes}")
    print(f"Attendance     : {percentage:.2f}%")

    print("=" * 50)


# Add a student
print("\n--- Add Student ---")
add_student()

# Display all students
display_students()

# Search for a student
search_student()

# Mark attendance
mark_attendance()

# Display attendance percentage
display_attendance()