# Christina Mauldin

# 11/14/2024
# P3HW2 Salary Calculation
# Calculating and displaying an employee's regular pay, overtime pay, and gross pay based on the hours worked and pay rate.


# Get the user input for employee details
employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
print("----------------------------------------")

# Check for overtime and calculate pay
if hours_worked >= 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_hours = 40
else:
    overtime_hours = 0
    overtime_pay = 0
    regular_hours = hours_worked

# Calculating regular and gross pay
regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay


# Display the results
print()
print(f"Employee Name: {employee_name}")
print()
print("Hours Worked   Pay Rate   Overtime   OverTime Pay    RegHour Pay    Gross Pay ")
print("--------------------------------------------------------------------------------")
print(f"{hours_worked:<15}{pay_rate:<12}{overtime_hours:<12,.2f}${overtime_pay:<14,.2f}${regular_pay:<14,.2f}${gross_pay:<8,.2f}")
