# 🎓 Student Attendance Register

A console-based Python application for managing student attendance, calculating attendance percentages, and generating useful class-level insights.

## 📌 About the Project

Managing attendance manually can become difficult when the number of students increases. It can also take time to calculate individual attendance percentages and identify students whose attendance is low.

I developed this project as a simple attendance management system for faculty. The application allows students to be registered using unique Roll Numbers, attendance to be recorded, and attendance information to be viewed and analyzed through a menu-driven interface.

The main focus of the project is to keep attendance management simple, organized, and easy to understand.

---

## 🎯 Problem Understanding

The main problems addressed by this project are:

- Maintaining student records manually
- Recording attendance for individual students
- Finding a student's attendance quickly
- Calculating attendance percentages
- Identifying students with low attendance
- Correcting attendance mistakes
- Understanding the overall attendance condition of a class

The application provides these features through a single console-based system.

---

## ✨ Features

### Student Management

- Add a new student
- Unique Roll Number validation
- View all registered students
- Search students by Roll Number
- Validate student names and Roll Numbers

### Attendance Management

- Mark students as Present or Absent
- View individual attendance reports
- Maintain attendance history
- Update incorrect attendance records

### Attendance Analysis

- Calculate individual attendance percentage
- Display class attendance summary
- Calculate average attendance
- Find highest and lowest attendance
- Identify students with attendance below 75%
- Display highest and lowest attendance students

### User Experience

- Menu-driven interface
- Input validation
- Error handling
- Clear console messages
- Organized reports and summaries

---

## 🐍 Python Concepts Used

The project uses the following Python concepts:

- Variables
- Strings
- Integers
- Lists
- Dictionaries
- Conditional statements
- `for` loops
- `while` loops
- Functions
- User input using `input()`
- Output using `print()`
- String formatting
- Exception handling using `try-except`
- Basic problem solving

---

## 🗂️ Data Structure

Student information is stored using a Python dictionary.

Each student record contains:

```python
{
    "name": "Student Name",
    "attendance": ["P", "P", "A", "P"]
}