
# Christina Mauldin

#11/12/2024

#P2HW1

# Recreating P1HW2 and displaying results neatly



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
remaining_balance = budget - total_expenses

# Display results nicely
print("\n------------ Travel Expenses ------------")
print(f"{'Location:':<20} {destination}")
print(f"{'Initial Budget:':<20} ${budget:,.2f}")
print(f"{'Fuel:':<20} ${gas_expense:,.2f}")
print(f"{'Accommodation:':<20} ${accommodation_expense:,.2f}")
print(f"{'Food:':<20} ${food_expense:,.2f}")
print("-----------------------------------------")
print(f"{'Remaining Balance:':<20} ${remaining_balance:,.2f}")
