# Christina Mauldin

# 11/13/2024

# P2HW2

# collecting grades and puting them in a list


# Collect all grades from user
grade_module1 = float(input("Enter grade for Module 1: "))
grade_module2 = float(input("Enter grade for Module 2: "))
grade_module3 = float(input("Enter grade for Module 3: "))
grade_module4 = float(input("Enter grade for Module 4: "))
grade_module5 = float(input("Enter grade for Module 5: "))
grade_module6 = float(input("Enter grade for Module 6: "))

# Make grade list
grades = [grade_module1, grade_module2, grade_module3, grade_module4, grade_module5, grade_module6]

# Display the results
print("\n------------Results------------")
print("Lowest Grade:  ", min(grades))
print("Highest Grade: ", max(grades))
print("Sum of Grades: ", sum(grades))
average_grade = sum(grades) / len(grades)
print("Average:       ", format(average_grade, ".2f"))
print("-------------------------------")
