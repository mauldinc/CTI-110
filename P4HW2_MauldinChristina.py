# Christina Mauldin

# 11/11/2024

# P4HW2

# Calculating regular, overtime, and gross pay for multiple employees. also totaling the values and displaying results.


# Initialize variables for totals and employee count
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
employee_count = 0

# Start a loop to collect employee data
while True:
    # Ask the user for the employee's name
    employee_name = input("Enter employee's name or 'Done' to terminate: ")

    # Check if the user wants to terminate the program
    if employee_name.lower() == "done":
        break

    # Ask the user for pay rate and hours worked
    hours_worked = float(input(f"How many hours did {employee_name} work? "))
    pay_rate = float(input(f"What is {employee_name} pay rate? "))

    # Check for over time and calculate pay
    if hours_worked >= 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (pay_rate *1.5)
        regular_hours = 40
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_hours = hours_worked

    # Calculate regular and gross pay
        regular_pay = hours_worked * pay_rate
        gross_pay = regular_pay + overtime_pay

    # Update totals
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay
    employee_count += 1

    # Display individual employee's pay details
    print()
    print(f"Employee Name: {employee_name}")
    print()
    print("Hours Worked   Pay Rate   Overtime   OverTime Pay    RegHour Pay    Gross Pay ")
    print("--------------------------------------------------------------------------------")
    print(f"{hours_worked:<15}{pay_rate:<12}{overtime_hours:<12,.2f}${overtime_pay:<14,.2f}${regular_pay:<14,.2f}${gross_pay:<8,.2f}")
    print()


# Display final totals
print()
print(f"Total number of employees entered: {employee_count:}")
print(f"Total Overtime Pay: ${total_overtime_pay:.2f}")
print(f"Total Regular Pay: ${total_regular_pay:.2f}")
print(f"Total Gross Pay: ${total_gross_pay:.2f}")

