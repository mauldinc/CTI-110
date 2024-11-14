# Christina Mauldin

#11/14/2024

#P3HW1 

# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules

mod_1 = float(input("Enter grade for Module 1: "))
mod_2 = float(input("Enter grade for Module 2: "))
mod_3 = float(input("Enter grade for Module 3: "))
mod_4 = float(input("Enter grade for Module 4: "))
mod_5 = float(input("Enter grade for Module 5: "))
mod_6 = float(input("Enter grade for Module 6: "))

# add grades entered to a list

grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest , sum and average for grades

low = min(grades)
high = max(grades)
total = sum(grades)
average = total / len(grades)

# determine letter grade for average
if average >= 90:
    letter_grade = 'A'
elif average >= 80:
    letter_grade = 'B'
elif average >= 70:
    letter_grade = 'C'
elif average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Display the results
print("\n------------Results----------")
print("Lowest Grade: ", low)
print("Highest Grade: ", high)
print("Sum of Grades: ", total)
print("Average:       ", format(average, ".2f"))
print("------------------------------")
print("Letter Grade: ", letter_grade)






