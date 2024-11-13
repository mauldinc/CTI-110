# Christina Maudin
#10/3/2024
#P2LAB2
# Using dictionary with user input 

# Create the dictionary
cars = {"camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26}

# Gete the keys only
keys = cars.keys()
print(keys)
print()

# Promt the user to give one of the keys (car)
user_key = input("Enter a vehicle to see it's mpg: ")
print()

# Show user mpg for their selected car
print(f"The {user_key} gets {cars[user_key]} mpg.")

# Get amount miles to be driven
miles_to_drive = float(input(f"How many miles will you drive the {user_key}? "))

#calculate gallons needed to drive distance
gallons_needed = miles_to_drive/cars[user_key]

# Display gallons needed to user
print(f"{gallons_needed: .2f} of gas are needed to drive the {user_key} {miles_to_drive} miles")
