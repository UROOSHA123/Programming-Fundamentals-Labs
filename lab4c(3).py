# Take 'age' as input from user.
age = int(input("Enter your age:"))
# Check if the person is less than 2 years old.
if age < 2 :
    print("The person is 'Baby'")
# Check if the person is at least 2 years old but less than 4 years old.
elif age < 4 :
    print("The person is 'Toddler'")
# Check if the person is at least 4 years old but less than 13 years old.
elif age < 13 :
    print("The person is 'Kid'")
# Check if the person is at least 13 years old but less than 20 years old.    
elif age < 20 :
    print("The person is 'Teenager'")
# Check if the person is at least 20 years old but less than 65 years old.
elif age < 65 :
    print("The person is 'Adult'")
# Check if all conditions are false.
else :
    print("The person is 'Elder'")