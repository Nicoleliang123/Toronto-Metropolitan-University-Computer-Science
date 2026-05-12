#Chapter 2.1

#Write a program that examines three variables—x, y, and z—
#and prints the largest odd number among them. If none of them are odd, it
#should print a message to that effect.

x = int(input("Enter x value:"))
y = int(input("Enter y value:"))
z = int(input("Enter z value:"))

#Create a number list
num = [x, y, z]

#Those that are != 0 are odd numbers
#n in the number list if remainder of n is not zero, meaning odd
#"n" is variable that your checking
#"n in num", checking in the list, if <condition>

odd = [n for n in num if n % 2 != 0]

#If "odd" list is empty 
if not odd:
    print("None of them are odd.")

#Otherwise there are odd numbers
else:
    #Find the largest number in the odd list
    largest = max(odd)
    print("The largest odd number in the list is:", largest)

#-----------------------------------------------------------------
#Chapter 2.4

#Write a program that asks the user to input 10 integers, and
#then prints the largest odd number that was entered. If no odd number was
#entered, it should print a message to that effect.

#Create an integers empty list
integers = []

#For 10 integers loop
for i in range(10):
    
    #Ask user 10 interger number
    x = int(input(f"Enter interger number {i+1}:"))
    
    #Add x number into integers list as it loops
    integers.append(x)
   
#Checks odd number if contained in all 10 integers in the list
oddnumber = [n for n in integers if n % 2 != 0]
    
#If oddnumber is empty list
if not oddnumber:
    print("None of them are odd.")

#Otherwise, there are odd number
else:
    
    #Finds the largest number out of the selective odd number list
    largestn = max(oddnumber)
    print("The largest odd number in the list is:", largestn)