"""
PROBLEM DESCRIPTION:
This program reads a list of polynomials from an input text file, displays them to the user,
and allows the user to select which polynomial to evaluate. The user then enters a numeric value
for x, and the program computes the simplified polynomial, its derivative, and evaluates the
polynomial at the given x. The result is displayed and written to an output text file.


The program demonstrates all required CPS109 elements: variables, arithmetic expressions,
if/elif/else logic, lists and sequence operations, for-loops, while-loops, user-defined
functions, file I/O, and formatted output. It is designed to operate in restricted execution
environments safely.
"""

import math

INPUT_FILE = "cps109_a1_input.txt"
OUTPUT_FILE = "cps109_a1_output.txt"

#----------------------------------------------------------
''' 
Turning polynomial inputs into a readable list (extract)
Example: -4x^2 + 7x + 1  
will turn into 
[(-4, 2), (7, 1), (1, 1)]   | (coefficient, exponent)
 
'''

#Conversion
def extract_polynomial(polynomial):
    
    #Remove extra spaces
    polynomial = polynomial.replace(" ", "")
    
    #Split into distinct sections 
    #replace all "-" with "+=" then split distinct sections for every "+"
    polynomial = polynomial.replace("-", "+-").split("+")
    
    #Create an empty list, represents each tuple (coefficient, exponent) of the whole polynomial list
    element_list = [] 
    
    #For every element in the polynomial list
    for element in polynomial:
        
        #Remove extra spaces
        element = element.strip()
        
        #If element/tuple one starts with empty, continue loop
        #(this can happen if first value is negative as we replace with "+=" and split "+"
        # which cause an result of " " empty)
        if element == "":
            continue
        
        #Case 1: If term = Constant (no x)
        if "x" not in element:
            
            #Convert string number into float
            coeff = float(element)
            
            #If constant, number value * 1 will always = constant number
            #No x, therefore x^0 gives 1
            exponent = 0
        
        #Case 2: If contains x
        else:
                
            #If x is positive
            if element == "x":
                coeff = 1 
                exponent = 1 
                
            #elif x is negative
            elif element == "-x":
                coeff = -1.0 
                exponent = 1 
            
            #otherwise if invovles coefficient and exponent
            else:
                
                #if in form 1: ax^n
                if 'x^' in element:
                    
                    #create new variable for the seperated string values of coeff & exp
                    #split into 2 sections through variable "x^" 
                    coeff_str, exponent_str = element.split("x^")
                    
                    #In the case in the form of x^n, will leave an "" coefficient string
                    #Naturally "x" has an coefficient value 1 
                    if coeff_str == "":
                        coeff = 1 
                    
                    #Otherwise
                    else:
                        
                        #convert coefficient into float for later math calculations
                        #exponent is not converted because not needed for later
                        coeff = float(coeff_str)
                        
                    # exponent
                    exponent = int(exponent_str)

                #If in form 2: ax 
                else:
                    
                    #This will leave only the coefficient hanging
                    #3x --> 3 
                    coeff_str = element.replace("x","")
                    
                    #Exponent will always be 1 in this scenario
                    exponent = 1
                    
                    #If the whole number is only left to be an ""
                    #Then it was given in the form "x"
                    #Which naturally has coefficient of 1 
                    if coeff_str == "":
                        coeff = 1 
                    
                    else:
                        
                        coeff = float(coeff_str)
        
        #Add tuple into element list
        element_list.append((coeff, exponent))
    
    return element_list

# ---------------------------------------------------------
# Function: combine_like_terms
# Combine terms with the same exponent by adding coefficients
# ---------------------------------------------------------

def combine_like_terms(element):
    
    #Create an dictionary
    #Through checking same exponent add coefficient value on top of each other (combine) 
    #Otherwise different exponent will just regularly add into dictionary without combining 
    element_dict = {}
    
    #For pairing of (coeff, exponent) in the list
    for coeff, exponent in element:
        
        #If exponent doesn't appear in dictionary
        if exponent not in element_dict:
            
            #Exponent is key to coeff 
            #Example Exponent = 2, Coeff = 3 then 2:3
            
            element_dict[exponent] = coeff
        
        #Otherwise exponent did appear in dictionary before
        else:
            
            #Then add coeff value for that specific exponent that was already in the dictionary
            #To combine like terms
            element_dict[exponent] += coeff
    
    #Create an list that extracts out any coefficient that was added to 0 
    #after combining like terms 
    extract_element = []
    
    #For (exponent, coeff) in dictionary items terms
    for exponent, coeff in element_dict.items():
        
        #If coefficient is not equal to 0
        if coeff != 0:
            
            #Then append the tuple into the new list
            extract_element.append((coeff, exponent))
    
    #As polynomial functions goes from the order of descending in exponents 
    #For each tuple t, take the second element (exponent)
    #Reverse=True will sort from largest to smallest for exponents
    
    extract_element.sort(key=lambda t: t[1], reverse=True)
    
    
    return extract_element 

#Function: element_to_str()
#Convert the list of (coefficient, exponent) tuple pairs back into
#Polynomial string (ex: 3x^2 - 2x + 1)

def element_to_str(element):
    
    #If list is empty, must be 0 
    if not element:
        return "0"
    
    #Create an empty result string
    result = "" 
    
    #Loop through each element in the list
    #Allow an tracker of position in list with "index"
    #This can allow seperation of coeff and exponent out of tuple
    for index, (coeff, exponent) in enumerate(element):
        
        #Determine coefficient positive or negative
        #If coefficient is less then 0, then negative
        if coeff < 0:
            sign = "-"
            
            #Get absolute value of coefficient
            #Formatting purpose
            #Can extract number seperately, as sign is already extracted
            abs_coeff = -coeff
            
        else:
            sign = "+"
            
            abs_coeff = coeff
    
        #Format element based on exponent
        if exponent == 0 :

            #no x, constant element
            element_str = str(abs_coeff)

        elif exponent == 1:

            #linear (x^1), don't show exponent as its unecessary 
            if abs_coeff == 1:

                #naturally, 1x = x
                element_str = "x"

            else:
            
                #f for formatting
                element_str = f"{abs_coeff}x"
    
        #If exponent is greater then 1
        else:
        
            if abs_coeff == 1:
            
                element_str = f"x^{exponent}"
        
            else:
            
                element_str = f"{abs_coeff}x^{exponent}"
    
        #Add the element to the output string with the corresponding sign
        if index == 0:
        
            #If coefficient is less then 0
            if coeff < 0:
            
                #Result: coeff is negative, & combine sign & number
                result += "-" + element_str
        
            else:
            
                #Otherwise, coefficient is positive
                #Naturally, ignore sign, just add number
                result += element_str
        
        else:
            
            result += " " + sign + " " + element_str
    return result

# ---------------------------------------------------------
# Function: derivative
# Calculate derivative of polynomial terms
# ---------------------------------------------------------

def derivative(element):
    
    #Create an empty list to store derivative elements
    deriv_element = []
    
    #Loop through each tuple in polynomial
    for coeff, exponent in element: 
        
        #Derivatives can only be taken with elemnt that has x
        #Exponent > 0 (not inclusive)
        
        if exponent > 0:
            
            #Apply power rule:
            #d/dx[coeff*x^exponent] = coeff*exponent*x^(exponent-1)
            
            #Add the result into the list
            deriv_element.append((coeff*exponent, exponent - 1))
    
    #Check to combine like terms for the derivative if exist & return
    return combine_like_terms(deriv_element)

# ---------------------------------------------------------
# Function: evaluate_terms
# Solves polynomial to calculate the resulting x value
# ---------------------------------------------------------
def evaluate_terms(element, x):
    
    #initialize total value for later result 
    total = 0.0
    
    #Loop through each element in the polynomial
    for coeff, exponent in element:
        
        #PApple power rule: #d/dx[coeff*x^exponent]
        total += coeff * (x ** exponent)
    
    #Returns value of polynomial at x
    return total

# ---------------------------------------------------------
# File I/O functions
# ---------------------------------------------------------

def read_input_file(path):
    
    #Return list of non-empty polynomial strings from file
    polynomials = []
    
    #Opens file at path in read mode ("r")
    with open(path, "r") as f:
        
        #Look at each line in file
        for line in f:
            
            #Remove spaces
            new_line = line.strip() 
            
            #If new line is not empty string
            if new_line != "":
                
                polynomials.append(new_line)
            
    #If file has no lines that are needed
    return polynomials

def write_output_file(path, lines):
    
    #Opens file at path in write mode ("w")
    with open(path, "w") as f:
        
        #Write all the string from the list "lines" into the file
        #Then add \n new line so that each line is on seperate line
        for line in lines:
            f.write(line +"\n")

#MAIN PROGRAM
def main():
    polynomials_input = read_input_file(INPUT_FILE)
    
    print("Available Polynomials:")
    for index, poly in enumerate(polynomials_input, 1):
        print(f"{index}: {poly}")
    
    #user chooses which polynomial to calculate
    while True:
        try: 
            choice = int(input(f"Enter the number of the polynomial to calculate/evaluate (1-{len(polynomials_input)}):"))
            if 1 <= choice <= len(polynomials_input):
                break
            else:
                print("Number out of range. Try again.")
        except ValueError:
            print("Invalid input. Enter an integer.")

    selection = polynomials_input[choice - 1]    
    
    #Entering the value for x
    while True:
        try:
            x_num = float(input("Enter the value of x:"))
            break
        except ValueError:
            print("Invalid input. Enter numeric value:")
            
    #Conversion of terms, simplifying, calculate the derivative and evaluate x value
    terms = combine_like_terms(extract_polynomial(selection))
    deriv = derivative(terms)
    x_result = evaluate_terms(terms, x_num)
    
    #Display results
    print("\nSimplified polynomial:", element_to_str(terms))
    print("Derivative:", element_to_str(deriv))
    print(f"Value at x = {x_num}: {x_result}")
    
    #Write result to output file
    output_lines = [f"Polynomial: {selection}",
                    f"Simplified: {element_to_str(terms)}",
                    f"Derivative: {element_to_str(deriv)}",
                    f"Value at x = {x_num}: {x_result}"]
    
    write_output_file(OUTPUT_FILE, output_lines)
    print(f"Results written to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()