# Christina Mauldin

#11/12/2024

#P1HW2

# Creating budget for a vaction



# Displaying what the program is 
print(f"This program calculates and displays travel expenses")
print()
# Ask user for information 
budget = float(input("Enter your Budget: $"))
print()
destination = input("Enter your travel destination: ")
print()
gas_expense = float(input(f"How much do you think you will spend on gas? $"))
print()
accommodation_expense = float(input(f"Approximately, How much will you need for accomodation/hotel? $"))
print()
food_expense = float(input(f"Last, How much do you need for food? $"))
print()
# Calculate the total expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Now subtract the expenses from the budget
remaining_budget = budget - total_expenses

# Display results
print("-------Travel Expenses--------")
print(f"Location: {destination}")
print(f"Initial Budget: ${budget}")
print()
print(f"Fuel: ${gas_expense}")
print(f"Accomodation: ${accommodation_expense}")
print(f"Food: ${food_expense}")
print()
print(f"Remaining Budget: ${remaining_budget:,.2f}")

