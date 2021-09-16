'''
TEMPERATURE PROGRAM
-------------------
Create a program that asks the user for a temperature in Fahrenheit, and then prints the temperature in Celsius.

Test with the following:

In: 32  Out: 0
In: 212  Out: 100
In: 52  Out: 11.1
In: 25  Out: -3.9
In: -40  Out: ??? Please tell me what this output is! (-40)

'''
print("Wellcom to Billy Bob's temperature decoder!")
F = float(input("What is the temperature in Fahrenheit? "))
C = (F-32) * (5/9)
print("It is ", C, "Degrees outside, thank you for using our services!")
