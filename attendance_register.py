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


# Add students
print("\n--- Add Student ---")
add_student()

# Display all students
display_students()