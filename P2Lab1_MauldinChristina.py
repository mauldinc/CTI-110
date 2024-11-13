# Christina Mauldin
#10/1/2024
# P2LAB1
# Using built-in libraries for cirlce circumference

# Import math library
import math

# Create a variable to hold pi
pi = math.pi

print(pi)
print()

# Get radius from user
radius = float(input("What is the radius of the circle? "))
print()

# Calculate/display the diameter
diameter = 2 * radius
print(f"The diameter of the circle is {diameter: .1f}\n")

# Calculate/display the circumference
circumf = 2 * pi * radius

# Round Variable to 2 decimal places
r_circumf = round(circumf, 2)

# Display 
print(f"The circumference of the circle is {circumf: .2f}\n")
print(f"The rounded Circumference of the circle is {r_circumf}\n")

# Calculate/display the area
area = math.pi * radius ** 2

area2 = math.pi * math.pow(radius, 2)

print(f"The area of the circle is {area: .3f}\n")
print(f"THe area of the circle is {area2: .3f}\n")
      
