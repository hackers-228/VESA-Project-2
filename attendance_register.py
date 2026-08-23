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


# Function to search for a student
def search_student():
    roll_number = input("\nEnter Roll Number to search: ").strip()

    if roll_number in students:
        student = students[roll_number]

        print("\n" + "=" * 50)
        print("             STUDENT DETAILS")
        print("=" * 50)
        print(f"Roll Number        : {roll_number}")
        print(f"Name               : {student['name']}")
        print(f"Attendance Records : {len(student['attendance'])}")
        print("=" * 50)

    else:
        print("\nStudent not found.")
        print("Please check the Roll Number and try again.")


# Function to mark attendance
def mark_attendance():
    roll_number = input("\nEnter Roll Number: ").strip()

    if roll_number not in students:
        print("Student not found.")
        return

    student = students[roll_number]

    print(f"\nStudent: {student['name']}")
    print("P - Present")
    print("A - Absent")

    status = input("Enter attendance status: ").strip().upper()

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

    return (present_classes / total_classes) * 100


# Function to display individual attendance
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


# Function to display class attendance summary
def attendance_summary():
    if not students:
        print("\nNo student records available.")
        return

    total_students = len(students)
    total_present = 0
    total_absent = 0
    students_with_attendance = 0

    for student in students.values():
        attendance = student["attendance"]

        if attendance:
            students_with_attendance += 1
            total_present += attendance.count("P")
            total_absent += attendance.count("A")

    total_classes_recorded = total_present + total_absent

    print("\n" + "=" * 50)
    print("          CLASS ATTENDANCE SUMMARY")
    print("=" * 50)

    print(f"Total Students       : {total_students}")
    print(f"Students with Record : {students_with_attendance}")
    print(f"Total Present        : {total_present}")
    print(f"Total Absent         : {total_absent}")
    print(f"Classes Recorded     : {total_classes_recorded}")

    if total_classes_recorded > 0:
        overall_percentage = (
            total_present / total_classes_recorded
        ) * 100

        print(f"Overall Attendance   : {overall_percentage:.2f}%")
    else:
        print("Overall Attendance   : 0.00%")

    print("=" * 50)


# Function to display attendance history
def attendance_history():
    roll_number = input("\nEnter Roll Number: ").strip()

    if roll_number not in students:
        print("Student not found.")
        return

    student = students[roll_number]
    attendance = student["attendance"]

    if not attendance:
        print("\nNo attendance history available.")
        return

    print("\n" + "=" * 50)
    print("           ATTENDANCE HISTORY")
    print("=" * 50)

    print(f"Roll Number : {roll_number}")
    print(f"Student     : {student['name']}")
    print()

    for i in range(len(attendance)):
        if attendance[i] == "P":
            status = "Present"
        else:
            status = "Absent"

        print(f"Class {i + 1:<3} : {status}")

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

# Display individual attendance
display_attendance()

# Display class summary
attendance_summary()

# Display attendance history
attendance_history()