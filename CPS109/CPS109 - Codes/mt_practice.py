def sum_follows(items):
    '''
    Assume that items is a list of integers. 
    How many groups of three consecutive integers, n1, n2, n3, satisfy
    the condition n1 + n2 == n3?
    Example:
        
        [1,1,2]
        grouping = 1
        
        explain: 1 + 1 = 2
        
        [1,1,2,3]
        grouping = 2
        
        explain: 1+1 = 2, 1+2 = 3
        
        [1,1,2,3,4]
        grouping = 2
        
        explain: 1+1 = 2, 1+2 = 3
        
        note: 2+3 does not equal 4, therefore only 2 groupings
    '''

    count = 0
    if len(items) < 3:
        return 0
    
    for i in range(len(items)-2):
        n1 = items[i]
        n2 = items[i+1]
        n3 = items[i+2]
        
        if n1 + n2 == n3:
            count += 1
    
    return count
