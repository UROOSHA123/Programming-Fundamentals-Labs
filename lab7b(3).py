 # Define a function with parameter n
def test_range(n):  
    # Check whether n is between 3 and 8
    if n in range(3, 9):
         # Display if inside range
        print(n, "is in the range")  
    else:
         # Display if outside
        print("The number is outside the given range.")  
# Call the function with different numbers
test_range(2)
test_range(7)
test_range(15)