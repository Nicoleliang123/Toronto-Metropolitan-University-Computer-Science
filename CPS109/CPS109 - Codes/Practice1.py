#Practice 1
#Bros Code

''' #1 Madlibs Game
Word game where you create a story by filling
in blanks with random words
'''
adjective1 = input("Enter an adjective (descriptive):")
noun1 = input("Enter an noun (person, place, thing):")
adjective2 = input ("Enter another adjective:")
verb1 = input("Enter an verb ending with 'ing': ")
adjective3 = input ("Enter last adjective:")
print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}")
print(f"I was {adjective3}!")

#----------------------------------------------------------
''' #2 Python Calculator
Create an python calculator where 
it allows users to choose which operations
to use between two variables for
+ - x / ^
'''

def addition(x,y):
    return x+y

def subtraction(x,y):
    return x-y

def multiplication(x,y):
    return x*y

def division(x,y):
    return x//y

def exponent(x,y):
    return x**y

x = float(input("Enter x value:"))
y = float(input("Enter y value:"))

#Automatically makes their input wording into lowercase 
#So that matching can be more likely
operation = input("Which operation (lowercase):").lower()

#While True will keep looping on forever
while True:
    
    if operation == "exponent":
        print(f"Your result of {x}^{y} is: {exponent(x,y)}")
        
        #If matches, prints out inner block code and will break the whole loop
        #Will not continue the rest of the loop block
        break
    
    elif operation == "division":
        print(f"Your result of {x}/{y} is: {division(x,y)}")
        break

    elif operation == "multiplication":
        print(f"Your result of {x}x{y} is: {multiplication(x,y)}")
        break
    
    elif operation == "subtraction":
        print(f"Your result of {x}-{y} is: {subtraction(x,y)}")
        break
    
    elif operation == "addition":
        print(f"Your result of {x}+{y} is: {addition(x,y)}")
        break
    
    #Otherwise if not these inputs, loops will become continous and keep looping
    else:
        operation = input("Invalid input. Please re-enter:").lower()
    
#----------------------------------------------------------------------------
''' #3. Python Weight Converter
Converting Kg to LBS or LBS to Kg of their weight
''' 

weight = float(input("Enter your weight:"))
unit = input("Enter kg or lbs:").lower() 

#While kept true, keep looping
while True:
    if unit == "kg":
        result = weight * 2.2 
        print("From Kg to Lbs")
        
        #Round result by 2 digit place
        print(f"Your weight from {weight}kg will turn into {round(result,2)}lbs.")
        break
    
    elif unit == "lbs":
        result = weight / 2.205
        print("From lbs to kg")
        print(f"Your weight from {weight}lbs will turn into {round(result,2)}kgs")
        break
    
    else:
        
        #makes sure that the re-enter is also considered lowercase
        unit = input("Invalid input, Please re-enter kg or lbs:").lower()
        
#---------------------------------------------------------------------------
''' #4. Temperature conversion 
Converting from fahrenheit to celcius or vice versa 
'''

temperature = float(input("Enter the temperature:"))
temp_type = input("Enter fahrenheit or celcius:").lower()

while True:
    if temp_type == "fahrenheit":
        result = (temperature - 32) / 1.8
        print("From fahrenehit to celsius")
        print(f"Temperature {temperature} fahrenehit is {result:.1f} celsius")
        break
    
    elif temp_type == "celcius":
        result = (temperature * 1.8) + 32
        print("From celcius to fahrenehit")
        print(f"Temperature {temperature} celsius is {result:.1f} fahrenheit")
        break
    
    else:
        temp_type = input("Invalid Input. Re-enter fahrenheit or celcius").lower()

#---------------------------------------------------------------------------
''' #5. Python compound interest calculator
Interest is the charge for borrowing money
A = P(1+r/n)^t
'''

#Set initial of principle, rate & time
principle = 0
rate = 0
time = 0

#While principle is less then 0, so it keeps looping until amount put in 
while principle <= 0:
    principle = float(input("Enter the principle amount:"))
    
    #If principle is less or equal to 0
    if principle <= 0:
        print("Principle can't be less than or equal to zero")

#While rate is less then 0, keep looping
while rate <= 0:
    rate = float(input("Enter the interest rate amount:"))
    if rate <= 0:
        print("Interest rate can't be less than or equal to zero")

#While time is less then 0, keep looping
while time <= 0:
    time = float(input("Enter the time in years:"))
    if time <= 0:
        print("Time can't be less than or equal to zero")

#Total amount
#pow() means (variable, power to another var)
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")

#----------------------------------------------------------------------------
''' #6. Shopping cart program
Will contain two list: foods & prices
Ask user what food they would like to buy
'''

#Empty list, so it's ordered
foods = []
prices = []

#Setting initial of total value
total = 0

#Loop forever
while True:
    food = input("Enter a food to buy (q to quit):")
    
    #If food lower version is the same as q, quit
    if food.lower() == "q":
        print("Program quitted.")
        break
    else:
        price = float(input(f"Enter the price of a {food}: $"))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price
    print()
    print(f"Your total is: ${total}")

#--------------------------------------------------------------------------
''' #7. Python number guessing game
Program will choose an random number from the range of 1-100
User must guess that exact number to end the program and win
'''
import random

lowest = 1
highest = 100
answer = random.randint(lowest, highest)

guesses = 0
keepgoing = True

print("Python Number Guessing Game")

while keepgoing:
    user = input(f"Guess the number between {lowest} and {highest}:")
    
    #isdigit() can only be used on strings
    if user.isdigit():
        
       # for later comparison of user guess and low/high
       # it must change itself from str to int to work
        user = int(user)
        
        #Guess will increase as keepgoing is true
        guesses += 1
        
        if user < lowest or user > highest:
            print("Invalid Guess. Out of range.")
            user = int(input(f"Guess the number between {lowest} and {highest}:"))
        
        elif user < answer:
            print("Low. Try again")
        
        elif user > answer:
            print("High. Try again")
        
        else:
            print(f"Correct! The answer was {answer}.")
            print(f"It took you {guesses}!")
            keepgoing = False
            
    else:
        print("Invalid Guess")
        user = int(input(f"Guess the number between {lowest} and {highest}:"))

#--------------------------------------------------------------------------------
''' #8. Rock, papers, scissors game
User plays against computer for 3 rounds, and shows whos the winner
'''

import random

#List of options
options = ("rock", "paper", "scissors")

#Counter
pcount = 0
ccount = 0

#Rounds set to best of 3
rounds = 3

#Introduction
print("Rock, Papers, Scissors Game against Computer")
print("Up to 3 rounds, Best of 3.\n")
playername = input("Enter your name:")

#Start at 1st round and ends at 4 not inclusive
for i in range (1, rounds+1):
    print(f"Round {i}:")
    
    #Converts all capital into lower
    p_choice = input("Enter your choice (rock, paper, scissors):").lower()
    
    #While players choice is not an element of the list, reprompt
    while p_choice not in options:
        p_choice = input("Invalid. Enter your choice (rock, paper, scissors):").lower()
   
    #random.randint() works with numbers
    #choice allows from tuple
    computer = random.choice(options)
    print(f"{playername}: {p_choice}")
    print(f"Computer: {computer}\n")
    
    if p_choice == computer:
        print("It's a tie!")
        
    elif p_choice == "rock" and computer == "scissors":
        print("You win!")
        pcount += 1
        
    elif p_choice == "paper" and computer == "rock":
        print("You win!")
        pcount += 1
        
    elif p_choice == "scissors" and computer == "paper":
        print("You win!")
        pcount += 1
        
    else:
        print("You lose")
        ccount += 1
    
    #If best of 3, one gets 2/3, break the whole loop
    if pcount == 2 or ccount == 2:
        break

print("----- FINAL RESULTS -----")
if pcount >= 2:
    print(f"{playername} wins the game by {pcount} wins")

elif ccount >= 2:
    print(f"Computer wins the game by {ccount} wins")

else:
    print("Nobody wins due to tie.")
    print(f"{playername}: {pcount} wins")
    print(f"Computer: {ccount} wins")

#----------------------------------------------------------------

''' #9. Dice Rolling Game
Compete dice rolling game with Computer
Two die will be added up to an sum
Whoever sum is bigger wins that round
for 3 rounds, whoever best out of 3, wins.
'''

import random

player_count = 0
computer_count = 0
rounds = 3

print("Dice Rolling Game, Best of 3")

player_name = input("Enter your name:\n")

choice = input("Would you like to start 'Roll the Dice' (y/n):").lower()


#If choice is yes
if choice == "y":
    
    #For the range starting from 1, up to 4 not inclusive
    for i in range(1, rounds+1):
        
        #Indicate what round, times of loop its on
        print(f"----Round {i}----")
        
        #Computer randomizes dice from 1-6
        computer_die1 = random.randint(1,6)
        computer_die2 = random.randint(1,6)
        
        #Computer sum
        c_result = computer_die1 + computer_die2
        
        #Player randomizes dice
        player_die1 = random.randint(1,6)
        player_die2 = random.randint(1,6)
        
        #Player sum
        p_result = player_die1 + player_die2
        
        #If sum of computer and player are the same, tie
        if c_result == p_result:
            print(f"There is an tie! Both sum are {p_result}.")
        
        #If computer sum greater then player
        elif c_result > p_result:
            print(f"Computer sum of {c_result} is bigger then {p_result}.")
            
            #Add a winning counter onto computer
            computer_count += 1
        
        #Otherwise player greater
        else:
            print(f"{player_name} sum of {p_result} is bigger then Computer's sum of {c_result}")
            
            #Winning counter onto player
            player_count += 1
        
        #If any of their count have 2 wins, then automatically they win so break loop
        if computer_count == 2 or player_count == 2:
            break
    
    #Comparing results
    print("-----RESULTS-----")
    if computer_count >= 2:
        print(f"Computer wins by {computer_count} rounds")
    
    elif player_count >= 2:
         (f"{player_name} wins by {player_count} rounds")
    
    else:
        print("Nobody Wins")

#Otherwise choice is no, program stopps
else:
    print("Program stopped.")

#------------------------------------------------------------------------------
    

