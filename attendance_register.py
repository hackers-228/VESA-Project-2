# --------------------------------------------
# Student Attendance Register
# VESA Skill Development Program - Project 2
# Domain: Python Programming
# --------------------------------------------

APP_TITLE = "STUDENT ATTENDANCE REGISTER"
ATTENDANCE_THRESHOLD = 75

# Dictionary to store all student records
students = {}

def print_separator():
    print("=" * 50)

def get_student():
    roll_number = input("Enter Roll Number: ").strip()

    if roll_number not in students:
        print("Student not found.")
        return None

    return roll_number


# Function to add a new student
def add_student():
    roll_number = input("Enter Roll Number: ").strip()

    if not roll_number:
        print("Roll Number cannot be empty.")
        return

    if not roll_number.isdigit():
        print("Roll Number must contain only numbers.")
        return

    if roll_number in students:
        print("Error: This Roll Number is already registered.")
        return

    name = input("Enter Student Name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    if not all(character.isalpha() or character.isspace() for character in name):
        print("Student name should contain only letters and spaces.")
        return

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
    if not students:
        print("\nNo students are registered.")
        return

    roll_number = input("\nEnter Roll Number: ").strip()

    if roll_number not in students:
        print("Student not found.")
        return

    student = students[roll_number]

    print(f"\nStudent: {student['name']}")
    print("P - Present")
    print("A - Absent")

    while True:
     status = input(
        "Enter attendance status (P/A): "
    ).strip().upper()

     if status == "P":
        student["attendance"].append("P")
        print("Attendance marked as Present.")
        break

     elif status == "A":
        student["attendance"].append("A")
        print("Attendance marked as Absent.")
        break

     else:
        print("Invalid input.")
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

    if total_classes > 0:
        if percentage < ATTENDANCE_THRESHOLD:
            print("Warning: Attendance is below 75%.")
        else:
            print("Status: Attendance is satisfactory.")

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
        status = "Present" if attendance[i] == "P" else "Absent"
        print(f"Class {i + 1:<3} : {status}")

    print("=" * 50)


# Function to update an attendance record
def update_attendance():
    roll_number = input("\nEnter Roll Number: ").strip()

    if roll_number not in students:
        print("Student not found.")
        return

    attendance = students[roll_number]["attendance"]

    if not attendance:
        print("No attendance records available for this student.")
        return

    print("\nCurrent Attendance:")

    for i in range(len(attendance)):
        status = "Present" if attendance[i] == "P" else "Absent"
        print(f"Class {i + 1}: {status}")

    try:
        class_number = int(input("Enter class number to update: ").strip())
    except ValueError:
        print("Class number must be a valid integer.")
        return

    if class_number < 1 or class_number > len(attendance):
        print("Invalid class number.")
        return

    new_status = input(
        "Enter new status (P for Present / A for Absent): "
    ).strip().upper()

    if new_status not in ["P", "A"]:
        print("Invalid attendance status.")
        return

    old_status = attendance[class_number - 1]
    attendance[class_number - 1] = new_status

    old_status_text = "Present" if old_status == "P" else "Absent"
    new_status_text = "Present" if new_status == "P" else "Absent"

    print(
        f"Attendance updated from {old_status_text} "
        f"to {new_status_text}."
    )


# Function to display students with low attendance
def low_attendance_students():
    print("\n" + "=" * 50)
    print("          LOW ATTENDANCE STUDENTS")
    print("=" * 50)

    found = False

    for roll_number, student in students.items():
        attendance = student["attendance"]

        if attendance:
            percentage = calculate_percentage(attendance)

            if percentage < ATTENDANCE_THRESHOLD:
                found = True

                print(f"Roll Number : {roll_number}")
                print(f"Name        : {student['name']}")
                print(f"Attendance  : {percentage:.2f}%")
                print("-" * 50)

    if not found:
        print("No students currently have low attendance.")

    print("=" * 50)


# Function to display class statistics
def class_statistics():
    if not students:
        print("\nNo student records available.")
        return

    attendance_percentages = []
    total_present = 0
    total_absent = 0

    for student in students.values():
        attendance = student["attendance"]

        if attendance:
            percentage = calculate_percentage(attendance)
            attendance_percentages.append(percentage)

            total_present += attendance.count("P")
            total_absent += attendance.count("A")

    print("\n" + "=" * 50)
    print("          CLASS ATTENDANCE STATISTICS")
    print("=" * 50)

    print(f"Total Students : {len(students)}")
    print(f"Present Records: {total_present}")
    print(f"Absent Records : {total_absent}")

    if attendance_percentages:
        average_attendance = (
            sum(attendance_percentages)
            / len(attendance_percentages)
        )

        highest_attendance = max(attendance_percentages)
        lowest_attendance = min(attendance_percentages)

        print(f"Average Attendance : {average_attendance:.2f}%")
        print(f"Highest Attendance : {highest_attendance:.2f}%")
        print(f"Lowest Attendance  : {lowest_attendance:.2f}%")
    else:
        print("No attendance has been recorded yet.")

    print("=" * 50)


# Function to display highest and lowest attendance students
def attendance_insights():
    student_percentages = []

    for roll_number, student in students.items():
        attendance = student["attendance"]

        if attendance:
            percentage = calculate_percentage(attendance)

            student_percentages.append(
                (percentage, roll_number, student["name"])
            )

    if not student_percentages:
        print("\nNo attendance data available for insights.")
        return

    highest = max(student_percentages)
    lowest = min(student_percentages)

    print("\n" + "=" * 50)
    print("          ATTENDANCE INSIGHTS")
    print("=" * 50)

    print(
        f"Highest Attendance : {highest[2]} "
        f"({highest[1]}) - {highest[0]:.2f}%"
    )

    print(
        f"Lowest Attendance  : {lowest[2]} "
        f"({lowest[1]}) - {lowest[0]:.2f}%"
    )

    print("=" * 50)


# Function to display the main menu
def display_menu():
    print("\n" + "=" * 50)
    print("              MAIN MENU")
    print("=" * 50)

    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Mark Attendance")
    print("5. View Attendance")
    print("6. View Attendance History")
    print("7. Update Attendance")
    print("8. Class Attendance Summary")
    print("9. Low Attendance Students")
    print("10. Class Statistics")
    print("11. Attendance Insights")
    print("12. Exit")

    print("=" * 50)


# Main program
print("\nWelcome to the Attendance Management System!")

def main():
    print("=" * 50)
    print(f"        {APP_TITLE}")
    print("=" * 50)
    print("Welcome to the Attendance Management System!")

    while True:
        display_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            display_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            mark_attendance()

        elif choice == "5":
            display_attendance()

        elif choice == "6":
            attendance_history()

        elif choice == "7":
            update_attendance()

        elif choice == "8":
            attendance_summary()

        elif choice == "9":
            low_attendance_students()

        elif choice == "10":
            class_statistics()

        elif choice == "11":
            attendance_insights()

        elif choice == "12":
            print("\nThank you for using Student Attendance Register.")
            print("Exiting program...")
            break

        else:
            print("\nInvalid menu choice.")
            print("Please enter a number between 1 and 12.")


if __name__ == "__main__":
    main()