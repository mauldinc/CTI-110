# Christina Mauldin

#11/14/2024

# P4Lab1A

# Using turtle to draw shapes

import turtle

win = turtle.Screen()
t = turtle.Turtle()

t.pensize(5)
t.pencolor("turquoise")
t.shape("arrow")


# Draw the square with for loop
for side in range(4):
    t.forward(200)
    t.left(90)

# Draw the triangle with while loop
sides = 3

while sides > 0:
    t.forward(200)
    t.left(120)
    sides = sides - 1
