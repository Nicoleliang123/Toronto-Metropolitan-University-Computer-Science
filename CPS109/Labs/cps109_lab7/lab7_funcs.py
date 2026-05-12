'''
No description needed at this point. Fill in the functions below
according to the description provided. 

These functions must be solved RECURSIVELY. If your solution does
not use recursion, you risk receiving a zero on the lab submission.

'''


# --------------------------------------------------------------
# 1) Count occurrences
# --------------------------------------------------------------

def count(items, target):

    '''
    This function emulates the list method 'count'. Assume items
    is a list, and target is some object. Return the number of
    times that target appears in items.
    
    YOU MUST USE RECURSION!    
    
    '''
    
    #If items is an empty list, return 0 as counter
    if items == []:
        return 0
    
    #If first item is the same as the target
    if items[0] == target:
        
        #Add one to counter, while items go to next index to the point it stopts to list
        return 1 + count(items[1:], target)
    
    #Otherwise, continue checking next (counter stays the same)
    else:
        return count(items[1:], target)

    
# --------------------------------------------------------------
# 2) Sum of integers
# --------------------------------------------------------------

def integer_sum(items):

    '''
    This function calculates and returns the sum of the integer
    values in the list 'items'.
    
    Be careful - items may contain things other than integers!
    
    For example, if the input is [ 1, 3, 'hello', 5.66 ], you 
    should return 4 (1 + 3).
    
    Hint: You can check if an object is an integer by performing 
    the following comparison: type(obj) == int
    
    YOU MUST USE RECURSION!    
    
    '''
    
    #If items list is empty
    if not items:
        return 0
    
    #initialize
    first = items[0]
    rest = items[1:]
    
    #If first is an integer
    if type(first) == int:
        
        #take and store first integer value and return back the rest of the list
        #for it to loop the next time
        return first + integer_sum(rest)
    
    #Otherwise check the rest
    else:
        return integer_sum(rest)

    
  
# --------------------------------------------------------------
# 3) Exponentiation
# --------------------------------------------------------------

def pow_rec(base, exponent):

    '''
    Assume that base and exponent are integers >= 0.
    
    Calculate and return base to the power of exponent using 
    repeated multiplications.
    
    YOU MUST USE RECURSION!

    '''
    
    #base case
    if exponent == 0:
        return 1
    
    
    return base * pow_rec(base, exponent - 1)
    
    
# --------------------------------------------------------------
# 4) Palindrome checker
# --------------------------------------------------------------

def is_palindrome(text):

    '''
    A recursion classic.
    
    Assume that 'text' is a string. Return True if text is a 
    palindrome, and False otherwise. 
    
    A string is a palindrome if it reads the same forwards and
    backwards. For example, 'racecar' is a palindrome.
    
    YOU MUST USE RECURSION!

    '''
    
    #base case - if text contains single character
    if len(text) <= 1:
        return True

    #checks if first and last character is different
    #then not palindrome
    if text[0] != text[-1]:
        return False

    #check inside substring and does recursive loop
    return is_palindrome(text[1:-1])

# --------------------------------------------------------------
# 5) Nested list reverser
# --------------------------------------------------------------

def nested_reverse(items):

    '''
    Assume that items is a list, that may contain nested lists
    as elements. This function will perform a reverse operation,
    but with a twist - nested sublists must be reveresed as well.
    
    For example, if the input is [ 1, 2, [5, 4, 3, [9, 0], 3 ] ]
    then you should return [ [ 3, [0, 9], 3, 4, 5], 2, 1 ]

    Hint: You can check if an object is a list by performing the 
    following comparison: type(obj) == list
    
    YOU MUST USE RECURSION!

    '''

    #If items list is emptylist
    if items == []:
        return []
 
    #Create an new list for reversed
    reversed_list = []
 
    #For the elements in items 
    for element in items[::-1]:
        
        #If that element is an list (subset)
        if type(element) == list:
            
            #add that subset list into the reversed
            reversed_list.append(nested_reverse(element))
        else:
            reversed_list.append(element)
 
    return reversed_list
