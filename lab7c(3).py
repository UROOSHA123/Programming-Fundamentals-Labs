# Define a function to find the GCD of two numbers
def gcd(a, b):
    # Repeat the process until b becomes zero
    while b != 0:
        # Find the remainder of a divided by b
        remainder = a % b
        # Assign the value of b to a
        a = b
        # Assign the remainder to b
        b = remainder
    # Return the GCD
    return a
# Call the function with two numbers
print("GCD is:", gcd(12, 27))