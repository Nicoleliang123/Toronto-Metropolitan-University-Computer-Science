# --------------------------------------------------------------
# 1) Summing Evens
# --------------------------------------------------------------
def sumeven(n):
    
    '''
    This function should calculate and return the sum of the 
    first n even numbers, where n >= 0. Note that 0 is even.
    
    For example, if n is 6, then the sum would be:

    0 + 2 + 4 + 6 + 8 + 10 = 30

    FOOD FOR THOUGHT:
    There are about a dozen different (yet equally 'good') ways 
    you could accomplish this. Once you've solved the problem,
    try solving it again using a different loop style, or a
    different way of producing the first n even integers. Or, 
    just maybe, you can come up with a way to solve this 
    without writing a loop at all?
    
    '''
    
    #formula for sum of even numbers
    valideven = n * (n-1)
    
    #if not number is not 0
    if valideven != 0:
        
        #return value of sum for even numbers
        return valideven
    
    #otherwise  n < 0, return 0 as sum
    else:
        return 0


# --------------------------------------------------------------
# 2) Summing Squares
# --------------------------------------------------------------
def sumsquares(n):
    
    '''
    This function should calculate and return the sum of the 
    first n squares, where n >= 0. Assume that 1 is the first 
    square.
    
    For example, if n is 5, then the sum would be:

    1 + 4 + 9 + 16 + 25 = 55
   
    FOOD FOR THOUGHT:
    How much code from your solution to the previous question
    can be reused? Work smart. It's not plagiarism if it's your
    own code you wrote previously!

    '''

    #formula for the sum
    validsquare = n * (n+1) * (2*n+1) // 6
    
    #if it is not >= 0, n < 0
    if validsquare != 0:
        
        #return that it is an valid square number, giving the sum
        return validsquare
    
    #other wise return 0, no squares to sum
    else:
        return 0



# --------------------------------------------------------------
# 3) Summing Odd Digits
# --------------------------------------------------------------   
def odddigitsum(num):
    
    '''
    This function should calculate and return the sum of the 
    odd digits in the input integer num. The input can be any 
    integer, positive or negative.
    
    For example, if num is 482376, then the sum would be:
    
    3 + 7 = 10
    
    FOOD FOR THOUGHT:
    One thing that sets computer scientists apart from 
    mathematicians is our appreciation for the integer 
    division (//) and remainder (%) operations. Why do I 
    bring this up here of all places...? 
    
    '''
    
    #gets the aboslute number value, ignore negative numbers
    num = abs(num)
    
    #create an sum total counter, initialize it at 0
    oddsum = 0
    
    while num > 0:
        
        #create an digit variable which only represents the LSB
        #LSB will then be used to determine odd/even
        digit = num % 10 
        
        #if odd, there is an remainder
        if digit % 2 != 0:
            
            #add that onto sum
            oddsum += digit
        
        #remove the last digit until value reaches to the end
        num //= 10
    
    #return the sum value, which includes 0 if it doesn't meet the while loop condition
    return oddsum    
    
    
# --------------------------------------------------------------
# 4) Listing Exponentials
# --------------------------------------------------------------
def listexponential(n, base):
    
    '''
    This function should calculate and return a list containing
    the first n exponentials, where 'base' is the base. Assume 
    that 0 is the first exponent.
    
    For example, if n is 6, and base is 2, then the list would be:
    
    [ 2**0, 2**1, 2**2, 2**3, 2**4, 2**5 ] = [ 1, 2, 4, 8, 16, 32]

    FOOD FOR THOUGHT:
    Use your solution to answer the age old thought experiment:
    Would you rather have $1,000,000 now, or $0.01 doubled
    every day for a month? 
   
    '''
    
    #create an empty list
    result = []
    #initilize the exponent 
    exponent = 0
    
    #while the exponent is smaller then input number
    while exponent < n:
        
        #create value variable for base to the exponent
        value = base ** exponent
        
        #add the value into the empty list
        result.append(value)
        
        #exponent value keep adding
        exponent += 1
    
    #return the result list, if while loop condition was not met,
    #it will print out an zero base list
    return result
    
    
# --------------------------------------------------------------
# 5) Concatenating Digits
# --------------------------------------------------------------      
def digitcat(s):
    
    '''
    This function accepts a string 's' as input, extracts the
    digit characters, and returns those digits as an integer.
    
    For example, if 's' is the string: 
    
    'I want 3 oranges, 24 bananas, and 101 dalmations'
    
    Then the function should return the integer 324101
    
    If there are no digits, return None.

    '''
    
    #create an empty string
    digits = ""
    
    #For every character in s
    for character in s:
        
        #Check if digit in 0-9
        if character.isdigit():
            
            #Add to digit string
            digits += character
    
    #If no digits found, "empty"
    if digits == "":
        
        return None
    
    #Otherwise, convert all digits that were gathered to integer
    else:
        return int(digits)
    
    
    
# --------------------------------------------------------------
# 6) Parsing Floats
# --------------------------------------------------------------      
def stringtofloatlist(fltstr):
    
    '''
    Given an input string guaranteed to contain comma-separated
    floating point numbers, extract each float and place them
    in a list. Return the list.
    
    For example, if the input string is "1.23,2.4,3.123", then
    you should return the list [ 1.23, 2.4, 3.123 ]
    
    FOOD FOR THOUGHT:
    Don't reinvent the wheel. Familiarize yourself with the 
    Python documentation. Perhaps there are some built-in string 
    methods (*cough* split() *cough*) that could be of service?
    https://docs.python.org/3/library/stdtypes.html#string-methods
    Alternatively, DO reinvent the wheel, it's great practice
    either way!
    
    '''
    
    if fltstr:
        #split() allows strings to be splitted up by ","
        result = fltstr.split(',')
        #convert into float
        result = [float(x) for x in result]
    
    #otherwise, empty list if string is empty
    else:
        result = []
    
    #return results
    return result
  

    
# --------------------------------------------------------------
# 7) Maximum of Each Type
# --------------------------------------------------------------      
def maxbytype(items):
    
    '''
    Assume that parameter 'items' is a heterogeneous list that
    may contain integers, floats, strings, and any other type.
    
    You should return a 3-tuple, where the first element is the
    largest integer, the second element is the largest float, 
    and the third element is the largest string.
    
    If any of the types are not found in the list at all, there
    can logically be no maximum, and therefore you should use 
    the value None to represent this.
    
    Example #1) if the input list is:
    [ "hello", 1, 3.14, 99, "cat", "tac", 2.7, "bat" ]
    Then the tuple returned should be: (99, 3.14, "tac")
    
    Example #2) if the input list is: 
    [ "hello", 1, 99, "cat", "tac", "bat" ]
    Then the tuple returned should be: (99, None, "tac")
    
    You can check the type of any object in Python by using the
    type() function. For example, type(item) == float, will 
    return True if item is a float, False otherwise.
    
    FOOD FOR THOUGHT:
    Why might we use the special value 'None' when there is no
    instance of a particular type present in the list? Why not
    use some error value, eg. -1 for integers, or the empty
    string if there is no string?

    '''
    
    #Largest integer, max if it is the lagest integer, otherwise none
    tupleint = max((x for x in items if type(x) == int), default=None)
    
    #Largest float
    tuplefloat = max((x for x in items if type(x) == float), default=None)
    
    #Largest string
    tuplestr = max((x for x in items if type(x) == str), default=None)
    
    #Return 3-tuple value
    return (tupleint, tuplefloat, tuplestr)
    

    

    
        
