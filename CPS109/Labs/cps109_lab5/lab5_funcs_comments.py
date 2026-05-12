# --------------------------------------------------------------
# 1) Mixed Fractions
# --------------------------------------------------------------

def mixedfraction(num, den):

    '''
    This function accepts an integer fraction, in the form of a
    numerator and a denominator. You may assume both numerator
    and denominator are non-negative.
    
    It returns a mixed fraction, 
    represented using a 3-tuple. The whole number is the first
    element, and the numerator and denominator of the remaining
    fraction are the 2nd and 3rd elements, respectively.
    
    For example:
    mixedfraction(7, 3) should return (2, 1, 3) 
    mixedfraction(4, 5) should return (0, 4, 5) 
    mixedfraction(9, 3) should return (3, 0, 3) 
    
    If the denominator is 0, return None.
    '''
    
    #If denominator is zero, return none
    if den == 0:
        return None
    
    #Whole number through numerator divided by denominator
    whole = num // den
    
    #The division of numerator over denominator gives an whole
    #The remainder number will become the new numerator
    remainder = num % den
    
    #Return in order
    return(whole, remainder, den)


# --------------------------------------------------------------
# 2) Cyclops Numbers
# --------------------------------------------------------------

def iscyclops(n):

    '''
    A non-negative integer is said to be a cyclops number if it 
    consists of an odd number of digits, the middle digit 
    (more poetically, the “eye”) is a zero, and all other 
    digits of that number are non-zero.

    Return True if the input is a cyclops number, and False
    otherwise.

    Note 1: Functions that return True/False are unlikely to 
    appear on a test, since you can achieve at least 50% by
    simply saying 'return True' or 'return False'...

    Note 2: This problem comes from Ilkka Kokkarinen's 
    excellent set of "109 Python Problems for CCPS 109". The 
    full set can be found at his github, and are great practice.

    https://github.com/ikokkari/PythonProblems

    Many (or most) of his problems are quite difficult, so be
    ready for a challenge if you attempt them.

    '''

    #Convert integer to string, for easy access
    cyclops = str(n)
    
    #Check digits if even
    if len(cyclops) % 2 == 0:
        #False
        return False
    
    #Find the middle digit placement of the number
    middledigit = len(cyclops) // 2
    
    #Check if middle digit of the number is zero
    if cyclops[middledigit] != '0':
        return False
    
    #Checks if other digits are non-zero
    #There should only be one zero in the whole number
    #Check if cyclops contain more than one '0'
    if cyclops.count('0') != 1:
        return False

    #Return True = Cyclops Number
    return True


# --------------------------------------------------------------
# 3) Parity Partition
# --------------------------------------------------------------

def paritypartition(items):

    '''
    This function accepts a list of integers, and returns a list
    containing the exact same integers, but separated by even
    and odd. All the even numbers should be at the front of the 
    list, and all the odd numbers should be at the back.

    The relative order of the even numbers should be the same
    as the original list. The same applies to the odd numbers.

    For example, given the input list:  [7, 0, 4, -1, 3, 2, 1]
    this function should return:        [0, 4, 2, 7, -1, 3, 1] 

    '''
    
    #Create empty sets for odd and even list
    odd = []
    even = []
    
    #For the numbers in the list
    #This will continue looping and adding until finished with all
    for num in items:
        
        #If the number is even
        if num % 2 == 0:
            
            #Add the number on to the list of even
            even.append(num)
        
        #Otherwise, add the number on to the list of odd
        else:
            odd.append(num)
    
    #Return even first, then odd
    return even + odd

# --------------------------------------------------------------
# 4) Alternating Sign Sum
# --------------------------------------------------------------

def altsignsum(items):

    '''
    This function accepts a list of positive numeric values, and 
    returns the alternating sign sum. 
    This means that elements in even index positions are added, 
    and elements at odd indexes are subtracted. For example:

    altsignsum([3, 5, 2, 4, 8, 2]) should return 2
    3 - 5 + 2 - 4 + 8 - 2 = 2

    If the input is the empty list, return 0

    ''' 
    
    #If items list is an empty list
    if not items:
        return 0
    
    #Initialize total sum value
    totalsum = 0
    
    #(index, element)
    #Checks for every index, and depending on position
    #element is either added or subtracted
    for index, element in enumerate(items):
        
        #If index position is even
        if index % 2 == 0:
            #Add element number to totalsum
            totalsum += element
        
        #Otherwise, odd, subtract element number to totalsum
        else:
            totalsum -= element
    
    #Return total sum value
    return totalsum

# --------------------------------------------------------------
# 5) Domino Cycle
# --------------------------------------------------------------

def domninocycle(tiles):

    '''
    This is another from Ilkka's problem set.

    A single domino tile is represented as a two-tuple of its 
    pip values, such as (2,5) or (6,6). This function should 
    determine whether the given list of tiles forms a cycle so 
    that each tile in the list ends with the exact same pip value 
    that its successor tile starts with, the successor of the 
    last tile being the first tile of the list since this is 
    supposed to be a cycle instead of a chain. 
    
    Return True if the given list of tiles forms such a cycle, 
    and False otherwise.

    For example, for the input  [(3, 5), (5, 2), (2, 3)], this
    function should return True.

    For the input [(2, 5), (5, 2), (2, 3)], this function 
    returns False because the first value on the first tile (2)
    does not match the 2nd value on the last tile (3)
    
    '''
    
    if not tiles:
        return True
    
    #If there is only one tile
    if len(tiles) == 1:
        
        #From tiles position pair 0, index 0
        #Must equal to position pair 0, index 1 
        #(Front and End) in order to create an cycle, which return True
        return tiles[0][0] == tiles[0][1]

    #Checks connections between each tile except the last one
    #Last one only checks backwards not forwards
    #Therefore tiles - 1
    for i in range(len(tiles) - 1):
        
        #second element of an pair of current tile
        second = tiles[i][1]
        
        #first element of the next pair 
        next_first = tiles[i + 1][0]
        
        if second != next_first:
            return False
        
    #Check closures of first tile and last tile
    initial = tiles[0][0]
    last = tiles[-1][1] 
    
    #Return true if first tile matches with last tile
    return initial == last