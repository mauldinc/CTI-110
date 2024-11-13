# Christina Mauldin

# 11/12/2024

#P1HW1

# Calculating integers


# Get the base and exponent from the user
print()
print("-----Calculating Exponents-----")
print()
base = int(input("Enter an integar as the base value: "))
exponent = int(input("Enter an integar for the exponent: "))
result = base ** exponent
print()

# Display the result 
print(f"{base} raised to the power of {exponent} is {result} !!")
print()

# Adding and subtracting three integars
print("-----Addition and Subtraction-----")
print()
num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter an integer to add: "))
num3 = int(input("Enter an integer to subtract: "))

# Perform the addition and subtraction
sum_result = num1 + num2
final_result = sum_result - num3

# Display the results
print()
print(f"{num1} + {num2} - {num3} is equal to {final_result}")
