# To ask the user to enter their score.
score = float(input("Enter your score: "))
# To check the score and assingn the grade.
if score >= 90.0:
    grade = 'A'
elif score >= 80.0:
    grade = 'B'
elif score >= 70.0:
    grade = 'C'
elif score >= 60.0:
    grade = 'D'
else:
    grade = 'F'
# To display the final grade.
print("Your grade is:" , grade)