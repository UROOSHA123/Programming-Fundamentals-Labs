# Define a function to check even or odd
def type_of_int(i):
    # Check if the remainder is zero
    if i % 2 == 0:
        return 'even' # Return even if divisible by 2
    else:
        return 'odd'  # Return odd otherwise 
# Call the function
print(type_of_int(9))
print(type_of_int(52))