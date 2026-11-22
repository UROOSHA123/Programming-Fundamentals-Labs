# Part c question 3
Functional_English = float(input("Enter marks of Functional English: "))
Linear_Algebra = float(input("Enter marks of Linear Algebra: "))
Digital_Logic_Design = float(input("Enter marks of Digital Logic Design: "))
Programming_Fundamentals = float(input("Enter marks of Programming Fundamentals: "))
Islamic_Studies = float(input("Enter marks of Islamic Studies: "))
Total = Functional_English + Linear_Algebra + Digital_Logic_Design + Programming_Fundamentals + Islamic_Studies
Average = Total / 5
Percentage = (Total * 100) / 250
print("\n-----RESULT-----")
print("Total Marks: ", Total)
print("Average: ", Average)
print("Percentage: ", Percentage, "")