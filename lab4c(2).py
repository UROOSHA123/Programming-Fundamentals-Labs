# Take years of service from the user. 
years = int(input("Enter years of service: "))
# Take qualification from the user
qualification = input("Enter qualification:")
# Check years of service and qualification.
if years >= 10 and qualification == "Masters":
    salary = 150000
elif years >= 10 and qualification == "Bachelors":
    salary = 100000
elif years < 10 and qualification == "Masters":
    salary = 100000 
elif years < 10 and qualification == "Bachelors":
    salary = 70000  
else: 
    salary = 0
# Display the calculated salary.
print("Your salary is RS.", salary)