# Display the message to the user
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)\n"
# Start an infinite loop
while True:
    # Ask the user to enter a city name
    city = input(prompt)
    # Check if the user wants to stop
    if city == "quit":
        break
    else:
        # Display the city name in title case
        print("I'd love to go to", city.title(), "!")