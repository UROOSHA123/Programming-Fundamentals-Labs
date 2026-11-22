# Take balance from the user
balance = float(input("Enter your balance: "))
# Start the loop
while True:
    # Check if balance is 9000 or less
    if balance <= 9000:
        # Increase the balance
        balance = balance + 999.99
    else:
        # Stop the loop when balance exceeds 9000
        break
# Display the final balance
print("Balance is", balance)