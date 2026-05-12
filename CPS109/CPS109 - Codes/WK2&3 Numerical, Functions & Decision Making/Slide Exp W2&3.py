#WEEK 2&3 EXP

#Write a program to say whether an integer x is even or odd and finish by printing 'all done'
x = int(input("Enter integer x:"))

if x % 2 == 0:
    print(x, "is even")
else:
    print(x, "is odd")

#-----------------------------------------
#Write a program using compound Boolean expressions
#that reports which out of x, y, z is the smallest number

xnum = int(input("Enter integer x:"))
ynum = int(input("Enter integer y:"))
znum = int(input("Enter integer z:"))

#X is least
if xnum <= ynum and xnum <= znum:
    print(xnum, "is the smallest out of:", xnum, ynum, znum)

#Y is least
elif ynum <= znum and ynum <= xnum:
    print(ynum, "is the smallest out of:", xnum, ynum, znum)

#Z is least
else:
    print(znum, "is the smallest out of:", xnum, ynum, znum) 

#---------------------------------------
#Write a function that accepts two arguments,
#representing the perpendicular edges of a right triangle.
#Calculate and return the length of the hypotenuse
#C = root(a^2 + b^2)

import math

#Create hypotenuse function, carry in a & b parameter
def hypotenuse(a,b):
    
    #Calculation
    hyp = math.sqrt(a**2 + b**2)
    
    #Return calculation value
    return hyp

# Ask the user for the two sides
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

#Result = a and b calculated in hypotenuse function 
result = hypotenuse(a,b)

#Round up result by 2 decimal places
print("The length of the hypotenuse is:", round(result, 2))    

#--------------------------------------------------
#Write functions that calculate the area and
#circumference of a circle, given the radius as input.

print("\n Circle Calculator")
radius = float(input("Enter the radius:"))

circumference = math.pi * 2 * radius
area = math.pi * radius ** 2

print(f"Circumference is: {circumference}")
print(f"Area is: {area}")

#---------------------------------------------------
#Version 2 with functions

def getcircumference(rad):
    circ = math.pi * 2 * rad
    return circ

def getarea(rad):
    area = math.pi * rad ** 2
    return area

print("\n Circle Calculator")
#Ask users for radius 
radius = float(input("Enter the radius:"))

#Put radius value into the function of area and circumference
#Causes functions to proceed with calculation
#Then return value
c = getcircumference(radius)
a = getarea(radius)

#Print value after return 
print(f"Circumference:{c}")
print(f"Area: {a}")

#-----------------------------------------------------
#Find and return the median of the three given parameters.
# a, b, c ---- The three values whose median to compute.
def median (a,b,c):
    a = float(input("Enter a value:"))
    b = float(input("Enter b value:"))
    c = float(input("Enter c value:"))

    #If a is the biggest, find the second biggest in b and c
    if a > b and a > c:
        return max(b, c)
    
    #If a is the smallest, find the second smallest in b and c
    elif a < b and a < c:
        return min(b, c)
    
    #Otherwise a is the median (middle number)
    else:
        return a

#------------------------------------------------------
#Determine whether the current year is a leap year. 

def is_leap_year(year):
    #If year is divisible by 4 and 400, consider leap year
    if year % 4 == 0 and year % 400 == 0:
        return True
    
    #Otherwise
    else:
        return False

#Ask user for input
y = int(input("Enter the current year:"))

#Print the result of T/F by inputing "y" value into leap year function
print(is_leap_year(y))

#------------------------------------------------------

