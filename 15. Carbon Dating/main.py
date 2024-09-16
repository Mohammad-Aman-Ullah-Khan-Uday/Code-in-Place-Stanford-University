"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!

Note: The starter code for this example is the solution.
"""

import math

K = -8266.64  # Half life constant

def main():
    calculate_age_single_sample()

def calculate_age_single_sample():
    """
    Gets user input for a percent of c14 left in a sample
    and then calculates the age of the sample based on that
    information, printing it out to the console.
    """
    
    # Ask the user to enter the percent c14 left in their sample
    pct_left = float(input("% of natural c14: "))
    
    # Calculate the age    
    age = K * math.log(pct_left / 100)
    
    # Print the result    
    print("Sample is " + str(age) + " years old.")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()