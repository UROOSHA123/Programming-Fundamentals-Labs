# Outer loop controls tables from 1 to 5
for i in range(1, 6):
    # Inner loop controls multiplication from 1 to 10
    for j in range(1, 11):
        # Calculate multiplication
        result = i * j
        # Display the multiplication table
        print(i, "*", j, "=", result)
    # Print a blank line after each table
    print()