# Nested for loops
# Outer loop runs from 0 to 4
for i in range(0, 5):
    # Inner loop runs according to the value of i
    for j in range(i):
        # Print the value of i on the same line
        print(i, end=' ')
    # Move to the next line
    print()