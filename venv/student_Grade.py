
# Student Grade Manager

name = input("Enter student name: ")
marks = float(input("Enter marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks! Enter marks between 0 and 100.")

elif marks >= 90:
    grade = "A"

elif marks >= 80:
    grade = "B"

elif marks >= 70:
    grade = "C"

elif marks >= 60:
    grade = "D"

elif marks >= 50:
    grade = "E"

else:
    grade = "F"

if 0 <= marks <= 100:
    print("\n--- Student Grade Report ---")
    print("Student Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)
