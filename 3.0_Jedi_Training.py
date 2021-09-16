# Sign your name:Will Jacobson
# In all the short programs below, do a good job communicating with your end user!


# 1.) Write a program that asks someone for their name and then prints a greeting that uses their name.
name = str(input("What is your name? "))
print("Hello", name)
# 2. Write a program where a user enters a base and height and you print the area of a triangle.
base = float(input("What is the base of the triangle? "))
height = float(input("What is the height of the triangle? "))
area = (base*height)/2
print("The triangle's area is", area)
# 3. Write a line of code that will ask the user for the radius of a circle and then prints the circumference.
import math

radius = float(input("What is the radius of your circle? "))
cir = (2*math.pi)*radius
print("Your circle's circumference is", cir)
# 4. Ask a user for an integer and then print the square root.
int = float(input("Name an integer. "))
sqrt = math.sqrt(int)
print("Your integer's square root is", sqrt)
# 5. Good Star Wars joke: "May the mass times acceleration be with you!" because F=ma.
#    Ask the user for mass and acceleration and then print out the Force on one line and "Get it?" on the next.
mass = float(input("What is the mass? "))
acceleration = float(input("What is the acceleration? "))
force = mass*acceleration
print("May the mass times acceleration be with you!", force, "Get it?")