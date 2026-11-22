# Check numbers from 900 to 1000
for num in range(900, 1001):
    # Skip even numbers
    if num % 2 == 0:
        continue
    # Check whether the number is prime
    for i in range(3, int(num ** 0.5) + 1, 2):
        # Check if the number is divisible
        if num % i == 0:
            break
    else:
        # Print the prime number
        print(num)