#WEEK 6

#Program that asks user to enter an email address
#Take the form <something1>@<something2>.com

while True:
    email = input("Enter email address:")
    
    at = email.find("@")
    dot = email.find(".")
    
    #if Find() can't find, then it returns -1
    if at == -1:
        print("Address must contain '@'")
        continue
    if dot == -1:
        print("Address must contain '.'")
        continue
    
    #start from 0 and ends "at"
    part1 = email[:at]
    
    #start from at + 1 l place, ends "dot"
    #Between @ and . 
    part2 = email[at+1:dot]
     
    #Start from dot+1 and onwards
    part3 = email[dot+1:]
    
    #If after dot, not com
    if part3 != "com":
        print("Address must end in '.com'")
        continue
    
    #If part1 or part 2 is empty
    if part1 == '' or part2 == '':
        print("Address cannot be empty")
        continue
    
    #isalnum checks if abc or num is present 
    #in which symbols cannot appear 
    
    #if part one is not aphanumeric, then it contains symbols
    if not part1.isalnum() or not part2.isalnum():
        print("Address must be alphanumeric")
        continue
    
    #If lowercase version of parts are not the same to original
    if part1.lower() != part1 or part2.lower() != part2:
        print("Address cannot contain capital letters")
        continue
    
    #If part one section, element 0 is a digit or part 2
    if part1[0].isdigit() or part2[0].isdigit():
        print("Address cannot begin with a numerical digit")
        continue
    
    print(f"Your email address is said to be: {email}")
    break

#------------------------------------------------------------------
