#Practice2

''' #1. Find the median of 3 integers
0.1 ) Use <= regular comparison
0.2 ) Use only < but with max/min help
'''

#0.1

def median(a,b,c):
    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <=c or c <= a <=b:
        return a
    else:
        return c

median()

#0.2

def median_2nd(a,b,c):
    if a > b and a > c:
        return max(b,c)
    elif a < b and a < c:
        return min(b,c)
    else:
        return a

''' #2. Determine how many days
there are in the given month.
'''

def days_in_month(month, leap_year = False):
    
    #If month is out of range then no days
    if month < 1 or month > 12:
        return 0 
    
    #If feburary, consider leap_year
    elif month == 2:
        
        if leap_year == True:
            
            #leap year = 29 days
            return 29
        else:
            return 28
    
    #Otherwise
    else:
        
        if month in (4,6,9,11):
            return 30
        else:
            return 31

''' #3. Determine if given year is an leap year
'''

def is_leap_year(year):
    if year % 4 == 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

''' #4. Determine if a list contains a sum 
to the exact goal.

Given a sorted list of items, see if it contains
two elements that exactly add up to goal.
If parameters i and j are given,
search through only within the sublist from 
i up to j, inclusive. 

Example:
nums = [1,2,4,6,10,14]
goal = 8
i = 1
j = 4

then only looks at [2,4,6,10]
since 2 + 6 = 8,
returns True

'''

def two_sums(items, goal, i=None, j=None):
    
    #If i or j is not provided, default as full range
    if i is None:
        
        #Set to default 1st element = 0
        i=0
        
    if j is None:
        
        #Last index will walways be length-1
        j = len(items) - 1
        
    # Keep looping forever as long i isnt done
    # Searches only between i and j
    while i < j:
        
        # Sum of values from most left to most right
        total = items[i] + items[j]
        
        # If sum is the same as goal
        # Pair up true
        if total == goal:
            return True
        
        # If sum is smaller then goal
        # Slowly increase from left
        elif total < goal:
            i += 1
        
        # Otherwise if sum is bigger then goal
        # Lower down value by decreasing from right
        else:
            j -= 1

    return False

