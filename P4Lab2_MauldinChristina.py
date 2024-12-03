# Christina Mauldin

# 11/14/2024

# P4LAB2

# Use while loop and for loop together


'''
Get integar from user
Determine if integar is positive or negative
if number is positive, diplay multiplication table
if the number is negative, tell user program cannot accept it
ask user to run again?
if yes, run program
if no, end program
'''


run_again = "yes"

while run_again != "no":
    
    user_num = int(input("Enter an integer: "))

    if user_num >= 0:
        #Display multiplication for that value and range (1-12)
        for item in range(1, 13):
            print(f"{user_num} * {item} = {user_num * item}")
    else:
        print()
        print("This program does not handle negative values")

    print()
    run_again = input("Would you like to run the program again? ")
    print()

# Loop has broken. User entered 'no'
print()
print("Program is ending....")


    



