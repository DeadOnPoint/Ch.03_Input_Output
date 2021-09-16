'''
TRAPEZOID PROGRAM
-------------------
Create a new program that will ask the user for the information needed to find the area of a trapezoid, and then print the area.

Test with the following:

base 1: 2       base 2: 3    height: 4    area: 10
base 1: 5       base 2: 7    height: 2    area: 12
base 1: 1       base 2: 2    height: 3    area: 4.5
base 1: 7       base 2: 2    height: 4    area: 18
'''

print("Welcome to trapezoidal calculations!")
b1 = float(input("What is the first base of the trapezoid? "))
b2 = float(input("What is the second base of the trapezoid? "))
h = float(input("What is the height of the trapezoid? "))
area = ((b1+b2)/2)*h
print("The area of the trapezoid is", area, "thank you for using our services today!")