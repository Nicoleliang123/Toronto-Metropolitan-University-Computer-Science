def rlen(num_list):
    
    #Base case
    if num_list == []:
        return 0
    
    else:

        #Add 1 to counter, while function moves on to next index
        return 1 + rlen(num_list[1:])
    

print(rlen([1,2,3,4,5,6]))

def rLen(num_list):
    
    #Base case
    if num_list == []:                
        return 0
    
    #Counter initialized
    count = 0
    
    #Initialize, the first index with the rest which iterates
    first, rest = num_list[0], num_list[1:]
    
    #
    if isinstance(first, list):   
        count += rLen(first)
    else:
        count += 1
    return count + rLen(rest)

#reverse a string
def rev_str(word):
    
    if len(word) <= 0:
        return ""
    
    elif len(word) == 1:
        return ""
    
    else:
        
        return rev_str(word[1:]) + word[0]

#summing the digits of a number
def digit(num):
    
    num = str(num)
    
    if len(num) == 1:
    
        return int(num)
    
    else:
        
        return digit(num[1:]) + int(num[0])

print(digit(552))
        