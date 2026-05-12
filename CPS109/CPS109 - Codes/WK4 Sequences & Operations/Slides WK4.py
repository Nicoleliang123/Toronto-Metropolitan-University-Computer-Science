#WEEK 4

#Prompts user to input a positive number from keyboard.
#Use for loop to calculate sum of all odd numbers up to 
#the inputted number, then while loop to 
#calculate sum of all even numbers up to the same number

def odd_number(num):
    
    #initialize odd
    sum_odd = 0
    
    #For number, start at one
    #increase by 2 steps until user's inputed value + one 
    #This ensures last number (input num) included
    for num in range(1, num+1, 2):
        
        #add number value into sum
        sum_odd += num 
    
    #return sum odd
    return sum_odd

def even_number(num):
    
    #initialize even
    sum_even = 0
    
    #Starting from 2
    #Step by 2
    for num in range(2, num+1, 2):
        
        sum_even += num
        
    return sum_even

num = int(input("Enter a positive number:"))

oddsum = odd_number(num)
evensum = even_number(num)

print("The sum of all odd numbers up to", num, "is:", oddsum)
print("The sum of all even numbers up to", num, "is:", evensum)

#---------------------------------------------------------------------------------
#Write program that reads radius from user until
#a radius of 0 is given. Calculate the area of the circle
#for each non-zero radius, using function aeraOfCircle().

def circle_area(radius):
    pi = 3.141
    return pi*radius*radius

radius = float(input("Enter the radius, 0 to quit:"))

#While radius is an positive value
while radius != 0:
    
    #If radius is smaller then 0
    if radius < 0:
        
        #area will = 0
        area = 0

    #otherwise if radius is bigger then 0, area is calculated
    else:
        area = circle_area(radius)
    
    #Print area
    #Repeat loop of input
    print("Area of circle with radius of", radius, "is", area)
    radius = float(input("Enter the radius, 0 to quit:"))

#Otherwise, it is == 0,program quit
else:
    print("Program quitted.")

#--------------------------------------------------------------------
#Write a function stars() that prints the following pattern. 
'''
*****
****
***
**
*
'''
#Write a program that uses that function several times

def stars():
    for i in range(5, 0, -1):
        print('*' * i)

stars()
print()
stars()

#----------------------------------------------------------------------
#Write a function perfectsquare(n) that resunts
#True if n is a perfect square, false otherwise

def perfectsquare(n):
    for i in range(n+1):
        square = i ** 2
        
        if square == n:
            return True
        if square > n:
            return False
    return False