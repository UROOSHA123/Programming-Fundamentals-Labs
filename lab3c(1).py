# Program to display student's biodata
# Take information from the user
name = input("Enter student name: ")
dob = input("Enter date of birth: ")
roll_no = input("Enter roll number: ")
section = input("Enter section: ")
# Take academic information
matric_percentage = float(input("Enter matric percentage: "))
matric_grade = input("Enter matric grade: ")
inter_percentage = float(input("Enter intermediate percentage: "))
inter_grade = input("Enter intermediate grade: ")
# Display student's biodata
print("\nStudent Biodata")
print("Name:", name)
print("Date of Birth:", dob)
print("Roll Number:", roll_no)
print("Section:", section)
print("Matric Percentage:", matric_percentage)
print("Matric Grade:", matric_grade)
print("Intermediate Percentage:", inter_percentage)
print("Intermediate Grade:", inter_grade)