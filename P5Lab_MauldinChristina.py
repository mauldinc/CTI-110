# Christina Mauldin

# 11/14/2024

# P5Lab

# Use main functions to simulate self-checkout

import random

def calcCashBack():
    # Generate a random float for amount owed to the store
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You Owe ${total_owed:.2f}")
    cash = float(input("How Much cash will you put in the self-checkout? $"))
    # Calculate cash back
    cash_back = cash - total_owed
    return cash_back


def disperseCashBack(change):
    
    #Convert the float value into an integer
    change = int(round(change * 100, 2))

    #print(change)

        
    if change == 0:
        print("No Change Due")

    #Calculate the amount of each coin needed
    #integer division - //

    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickles = change // 5
    change = change - (num_nickles *5)

    num_pennies = change // 1

    #Display coins owed

    if num_dollars > 0:
        print(num_dollars,  end=" ")
        if num_dollars == 1:
            print("Dollar")
        else:
            print("Dollars")
            
    if num_quarters > 0:
        print(num_quarters,  end=" ")
        if num_quarters == 1:
            print("Quarter")
        else:
            print("Quarters")

    if num_dimes > 0:
        print(num_dimes,  end=" ")
        if num_dimes == 1:
            print("Dime")
        else:
            print("Dimes")

    if num_nickles > 0:
        print(num_nickles,  end=" ")
        if num_nickles == 1:
            print("Nickle")
        else:
            print("Nickles")

    if num_pennies > 0:
        print(num_pennies,  end=" ")
        if num_pennies == 1:
            print("Penny")
        else:
            print("Pennies")
        


# Define the main
def main():
    print("*******Welcome to the self-checkout!!!*******")
    cash_back = calcCashBack()
    print(f"Change is ${cash_back:.2f}")
    disperseCashBack(cash_back)
    

# Call the main
if __name__ == "__main__":
    main()
