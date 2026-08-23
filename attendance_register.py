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
    name = input("Enter Student Name: ").strip()

    students[roll_number] = {
        "name": name,
        "attendance": []
    }

    print(f"\nStudent {name} added successfully.")


# Add students
print("\n--- Add Student ---")
add_student()

print("\nCurrent Student Records:")
print(students)