# Define a function to find the maximum of three numbers
def max(a, b, c):
    # Check if a is greater than or equal to b and c
    if a >= b and a >= c:
        return a  # Return a if it is the largest
    # Check if b is greater than or equal to a and c
    elif b >= a and b >= c:
        return b  # Return b if it is the largest
    else:
        return c  # Return c if it is the largest
# Call the function with three numbers
print(max(10, 25, 15))