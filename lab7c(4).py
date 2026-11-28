# Define a function with city and country parameters
# Iceland is the default country
def describe_city(city, country="Pakistan"):
    # Print a sentence using the city and country
    print(city + " is in " + country + ".")
# Call the function for a city in the default country
describe_city("Karachi")
# Call the function for another city in the default country
describe_city("Islamabad")
# Call the function for a city in a different country
describe_city("Mumbai", "India")