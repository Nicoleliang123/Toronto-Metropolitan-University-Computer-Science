#ChatGPT Prompts

'''#1. Shopping List Analyzer
Analyze a list of prices and items.
Ask user for 5 item prices and stores them into list.
Calculate the total, average, max and min.

Example:
Items: [('apple', 1.5), ('milk', 3.0), ('bread', 2.0)]
Total: 6.5 | Average: 2.17 | Max: 3.0 | Min: 1.5
'''

#Create empty tuple list
items = []

total = 0

#Prompt
for i in range (1,6):
    item = input(f"Enter item {i}:")
    price = float(input(f"Enter item {i} price:"))
    
    total += price
    
    
    #Add each item and price as one argument tuple
    #One tuple = one element of list
    items.append((item, price))

average = total / 5

#price variable for whatever var., specifically price in items list
max_price = max(price for food, price in items)

min_price = min(price for food, price in items)

print(items)
print(f"Total: {total} | Average: {average} | Max: {max_price} | Min: {min_price}")

#----------------------------------------------------------------------

''' #2. Temperature Converter List
Use a list to convert multiple Celsius values
into Fahrenheit
Given: F = (C x 9/5) + 32

Example:
    [0,10,20,30]
output: [32.0, 50.0, 68.0, 86.0]
'''

#No need to initialize list due to 
#not looping

c_values = input("Enter multiple celsius values (by comma): ")
    
#Split string by commas
#Create a list of strings
c_list = c_values.split(",") 

#For every c element in c_list, will be converted to float
c_list = [float(c) for c in c_list]

#Apply function for every c element in c list
f_list = [(c * 9/5) + 32 for c in c_list]
    
print(f_list)

#-----------------------------------------------------------------------

''' #3. Digital Root Finder
Repeatedly add digits of a number until 
one digit remains

Example:
num = 981
9 + 8 + 1 = 18
1 + 8 = 9

therefore output is 9 
'''

num = int(input("Enter number value:"))

#While length of string is bigger then one place
#Keep looping
while len(str(num)) > 1:
    
    #Initialize total value
    total = 0
    
    #For digit place in the string number
    for digit in str(num):
        
        #Add each int digit individually into total
        total += int(digit)
    
    #Total becomes new number and keeps looping
    #If applies to it
    num = total

print(f"Result: {num}")

#--------------------------------------------------------------------------
''' #4. Grading System
Write a function grade(score) returning a letter grade

Example:
A: 90–100  
B: 80–89  
C: 70–79  
D: 60–69  
F: below 60
'''

def grade(score):
    if score <= 100 and score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

score = int(input("Enter your score:"))

print(f"Your letter grade is: {grade(score)}")

#-----------------------------------------------------------------
''' #5. Factorial Calculator
Write a program to calculate the factorial
of a given number

Formula:
    n! = n x (n-1) x (n-2) x ... x 1

Example:
input = 5
output = 120
'''

def getfactorial(num):
    
    #initialize result as one
    #due to 0 can't be multipled
    result = 1
    
    #While number is still greater then 1
    #avoid going over the last factor
    while num > 1:
        
        #Result will multiply with current num
        result *= num
        
        #New num will be num -1
        num = num - 1
    
    #Return result, and continue
    return result

num = int(input("Enter the number:"))

print(f"The factorial is: {getfactorial(num)}")

#-------------------------------------------------------------
''' #6. Prime Number Checker
Ask user for a number 
Determine whether prime or not

Prime numbers:
    Have only 2 factors
    1 and themselves
    
    Such as 2,3,5,7,11
    
Example:
Input = 7
Output = 7 is a prime number
'''

number = int(input("Enter an integer:"))
if number <= 1:
    print(f"Integer {number} is not a prime number")
else:
    for i in range (2, number):
        if number % i == 0:
            print(f"Interger {number} is not a prime number.")
            break
        else:
            print(f"Interger {number} is an prime number")
                
#-------------------------------------------------------------------
''' #7. GCD & LCM Finder
Find the greatest common divisor 
and least common multiple of 2 numbers

Formula:
GCM(a,b) = largest number dividing both
LCM(a,b) = (a x b) / GCD(a,b)

Example:
Input = 12, 18
Output = GCD = 6, LCM = 36
'''

num1 = int(input("Enter first integer:"))
num2 = int(input("Enter second integer:"))

def get_gcd(a,b):
    
    #Keep replacing larger number with its remainder 
    #When divided by smaller one
    
    while b != 0:
        
        #a % b = new b value
        #While loop continues when not 0
        #Until reach b = 0, return a value = GCD
        a, b = b, a % b 
    return a

def get_lcm(a,b):
    return abs(a*b) // get_gcd(a,b)

print(f"GCD of {num1} and {num2} is: {get_gcd(num1, num2)}")
print(f"LCM of {num1} and {num2} is: {get_lcm(num1, num2)}")