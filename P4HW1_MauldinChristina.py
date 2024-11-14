# Christina Mauldin
#11/10/2024
#P4HW1
# using loop to display score average

# Get integer to run the main for loop
num_scores = int(input("How many scores do you want to enter? "))
print()
scores = []


# For loop to iterate num_scores times
for items in range(num_scores):
    while True:
        try:
            score = float(input(f"Enter score #{items+1}: "))
            if 0 <= score <= 100:
                scores.append(score)
                break
            else:
                print()
                print("INVALID Score entered!!!!")
                print("Scores should be between 0 and 100")
        except: 
            print("Enter score #{items+1} again: ")


# Calculating the lowest scores
lowest_score = min(scores)
scores.remove(lowest_score)

average_score = sum(scores) / len(scores)


# Determining letter grade
if average_score >= 90:
    letter_grade = 'A'
elif average_score >= 80:
    letter_grade = 'B'
elif average_score >= 70:
    letter_grade = 'C'
elif average_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'
    
print()
print()

# Diplaying results
print("--------------Results-----------")
print(f"Lowest Score  : {lowest_score}")
print(f"Modified List : {scores}")
print(f"Score Average : {average_score:.2f}")
print(f"Grade         : {letter_grade}")
print("------------------------------------")
