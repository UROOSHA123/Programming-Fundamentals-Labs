# Initialize total sum to zero
total = 0
# Run the outer loop from 1 to 7
for i in range(1, 8):
    # Initialize factorial to 1
    fact = 1
    # Calculate factorial of i
    for j in range(1, i + 1):
        fact = fact * j
    # Add each term to the total sum
    total = total + (i / fact)
# Display the final sum
print("Sum of the series is:", total)