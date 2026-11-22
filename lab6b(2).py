# LEFT SIDE:
# Assign values to three variables
i = 1
j = 2
k = 3
# Check if i is greater than j
if i > j:
# Check if i is greater than k
    if i > k:
        print('A')
# Execute if the outer condition is false
else:
    print('B')

# RIGHT SIDE:
# Assign values to three variables
i = 1
j = 2
k = 3
# Check if i is greater than j
if i > j:
    # Check if i is greater than k
    if i > k:
        print('A')
    # Execute if the inner if condition is false
    else:
        print('B')