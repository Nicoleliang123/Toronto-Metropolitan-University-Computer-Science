#PYNative Coding

''' #1. Multiplication & Sum of Integers
Given two integer numbers, write a Python program to return their product 
only if the product is equal to or lower than 1000. Otherwise, return their sum
'''

def calculation(x,y):
    
    #Product is the multiplication of 2 numbers
    product = x*y
    
    #If product is equal to a or less than 1000
    if product <= 1000:
        return product
    
    #Otherwise, only return their sum value
    else:
        return x+y

#Test values
print("Result is", calculation(20, 30))
print("Result is", calculation (30, 40))

''' #2. Sum of current and previous
Write Python code to iterate through the first 10 numbers and, in each iteration, 
print the sum of the current and previous number.
'''

#Initiate values for current & previous
current = 0
previous = 0

#For the range of the first 10 numbers
for i in range(10):
    
    #previous will be the current number initiating from 0
    previous = current
    
    #Print previous first
    print("P:", previous)
    
    #Current will then add the next number which i is increasing through iteration
    current += i
    
    #Then print current, for it to loop in proper order
    print("C:", current)
    
''' #3. Even characters
Write a Python code to accept a string from the user and display characters present 
at an even index number.
'''

string = "abcd"

def even_string(string):
    
    #Initiate an string  result
    result = ""
    
    #Iterate for however long string is
    for i in range(len(string)):
        
        #For each singular character, take string list index of i
        character = string[i]
        
        #If i due to starting from 0 add 1 % 2 is ==0
        if (i+1) % 2 == 0:
            
            #character value will be added to the result string
            result += character
    
    return result

print(even_string(string))

''' #4. Remove characters of String
Write a Python code to remove characters from a string from 0 to n and return a new string.
'''

n = "a1b2c3"

def remove_char(n):
    
    #initiate result string
    result = ""
    
    #iterate from 0 to th length of n value 
    for i in range(0, len(n)):
        
        #obtain character value from n list of i index
        character = n[i]
        
        #check if character (str.isdigit())
        if character.isdigit():
            
            #add character value into the result
            result += character
        
    return result

print(remove_char(n))
            
''' #5. Same value of beginning & end of list
Write a code to return True if the list's first and last numbers are the same.
If the numbers are different, return False. 
'''


value_list = [10,20,30,40,10]

#If value list index 0 and last index is equal
if value_list[0] == value_list[-1]:
    
    print("True")

else:
    
    print("False")

''' #6. Display numbers divisible by 5 ONLY
Write a code to display numbers from a list divisible by 5 only.
'''

division_list = [2, 30, 6, 45, 50, 60]

def divisible(division_list):
    
    #Create an empty list result
    result = []
    
    #Iterate through until the length of the list
    for i in range(len(division_list)):

        #Obtain value(element) from the list of index i
        element = division_list[i]
        
        #If element is divisible by 5
        if element % 5 == 0:

            #then add the element value into the result
            result.append(element)
    
    return result

print(divisible(division_list))
        
''' #7. Find the number of occurences of a substring in a string
Check to find how often substring "Emma" appears in the given string
'''

substring = "Emma"

given = "Emma is at school. She decides to buy lunch. At last Emma pays the bill.\n Emma finishes her day."

print (given.count("Emma"))

''' #9. Palindrome Number
Check if an given number is an palindrome. 
Palindrome reads the same forwards and backwards.
Example:
    545 is an palindrome number 
'''

result = 0
num = 12321
def if_palindrome(num):
    
    #Keep looping while the number is bigger then 0
    while num > 0:
        
        #Convert number into an string, to go backwards
        str_num = str(num)
        
        #Goes backwards and checks if same as original
        if str_num == str_num[::-1]:
            
            return True
        else:
        
            return False

print(if_palindrome(num))
