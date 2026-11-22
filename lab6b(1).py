# Assign 10 to variable 'i'
i = 10
# Check whether i is equal to 10
if (i == 10):
    # First if statement
    # Check whether i is smaller than 15
    if (i < 15):
        print("i is smaller than 15")
    # Nested if statement
    # Check whether i is smaller than 12
    # Executes only if the first if condition is true
    if (i < 12):
        print("i is smaller than 12 too")
    else:
        # Executes if the second if condition is false
        print("i is greater than 15")