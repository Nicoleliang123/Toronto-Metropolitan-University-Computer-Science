#Textbook W2&3

#Write a program that asks the user to enter an integer and
#prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal
#to the integer entered by the user. If no such pair of integers exists, it should
#print a message to that effect.

#Input
num = int(input("Enter an integer:"))

#Matching
match = False

#Power has to be 0 < pwr < 6
#Remember, one power won't work and doing up to 6 
#Will end at 5
for pwr in range(2,6):
    
    #Find possible roots
    #From -ve number to number + 1 as you can have range of roots
    #Inclusive of number itself by +1
    for root in range(-abs(num), abs(num)+1):
        
        #If root**pwr = number
        if root ** pwr == num:
            print("Root=", root, "Power=", pwr)
            
            match = True

#If not an matching pair
if not match:
    print("No such pair of integers exists.")
            
#----------------------------------------------------------------------
#Let s be a string that contains a sequence of decimal numbers
#separated by commas, e.g., s = '1.23,2.4,3.123'. Write a program that prints
#the sum of the numbers in s.

#Only put input because split can only be used on strings
#Therefore no float
s = input("Enter decimal numbers (seperated by commas):")

#Split the string into separate number strings
number = s.split(',')

#Sum at 0
sum = 0.0

#Go through each number string
for num_str in number:
    
    #Convert string to float
    converted = float(num_str)
    
    #Add to sum
    sum += converted

#Print result
print("The sum is:", sum)

#--------------------------------------------------------------------
#Write a function isIn that accepts two strings as arguments
#and returns True if either string occurs anywhere in the other, and False
#otherwise. Hint: you might want to use the built-in str operation in. 

def isIn(x,y):
    
    #If one string is an substring of the other, true
    if x in y or y in x:
        return True
    else:
        return False

x = input("Enter x string: ")
y = input ("Enter y string: ")

print(isIn(x,y))

#---------------------------------------------------------------------

