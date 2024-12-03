# Christina Mauldin

#11/14/2024

#P4Lab1b

# Using turtle to draw my intitials
import turtle
wn = turtle.Screen


# Customizing turtle
t = turtle.Turtle()
t.pensize(6)
t.pencolor("turquoise")
t.shape("arrow")
t.speed(10)

# Creating intitial C
for i in range(180):
    t.backward(1)
    t.left(1)

# Creating Initial M
t.penup()
t.goto(50, 0)
t.pendown()
t.setheading(90)
t.forward(100)
t.right(135)
t.forward(50 * 2**0.5)
t.left(135)
t.forward(50 * 2**0.5)
t.right(135)
t.forward(100)



    

