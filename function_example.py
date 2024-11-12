# Create user-defined functions

# Defined a non-value returning function
def my_animal(name, sound, pound_food):
    print(f"The{name} makes a {sound} noise!")
    print(f"The {name} eats {pound_food} pounds of food a day")
    print(f"The {name} eats {pound_food * 7} pounds of food a day")


# Create a main function - all logic goes here
def main(): 
    print("The main function is executing!")
    print()
    #Call the my_animal function
    my_animal("Lion", "Roar",20.6)

# Call the main Function
if __name__ == "__main__":
    main()
