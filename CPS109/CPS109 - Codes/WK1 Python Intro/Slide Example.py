import math

#Square root the argument 9 resulting 3.0
math.sqrt(9)

#Pi
math.pi

#Cosine of pi number
math.cos(math.pi)

#Sin of pi number
#Which should be zero
#Can't escape floating point = error
math.sin(math.pi)

#Rounds numbers (num, round to num decimal places)
round(3.333, 0)

#Ex: will equal to 0.0
round(math.sin(math.pi), 15)

#---------------------------------------------------

#\n acts as new line character
#\t inserts a tab
#\b does backspace

#automatically is string
num = input("\nEnter a number:")
print("Number:", num)

#converts to floating-point value
radius = float(input("Enter radius:"))

#allows calculations
circ = math.pi * 2 * radius
area = math.pi * radius ** 2

# "f" in front of the string, outside the quotes 
# {circ} inserts value from earlier into the string

#formatted string
print(f"Circumference = {circ}")
print(f"Area = {area}")

#----------------------------------------------------
#Odd/Even

#Ask user for input
x = int(input('Enter an integer:'))

#If remainder is 0 after division of 2, then it's even
if x%2 == 0:
    print(x, "is even")

#Otherwise odd
else:
    print(x, "is odd")

#---------------------------------------------------
#Nested Conditionals
#Divisibility by 2 and 3
a = int(input('Enter a:'))

#If divisible by 2 and remainder equals 0
if a%2 == 0:
    #divisible by 3
    if a%3 == 0:
        print(a,"is divisible by 2 and 3")
    else:
        print(a,"is divisible by 2 but not 3")
elif a%3 == 0:
    print(a,"is divisible by 3 and not 2")

#----------------------------------------------------
#Compound Booleans
#Check x,y,z which is least value
xvalue = int(input('Enter x:'))
yvalue = int(input('Enter y:'))
zvalue = int(input('Enter z:'))

#If x is smallest value, must be less then y and z
if xvalue < yvalue and xvalue < zvalue:
    print("x is least")

#Elif, if x is biggest, y is smaller then z
elif yvalue < zvalue:
    print ('y is least')

#Otherwise, x is biggest, y is second biggest
#Then z can only be least value
else:
    print ('z is least')

