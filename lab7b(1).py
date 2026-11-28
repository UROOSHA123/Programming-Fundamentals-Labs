# Define the outer function 
def test(a):
    # Define the inner function 
    def add(b):
        # Assign 1 to a
        a =+ 1
        # Return the sum of a and b 
        return a + b
    # Return the inner function  
    return add
# Store the returned function 
func = test(4)
# Call the inner function with 4
print(func(4))