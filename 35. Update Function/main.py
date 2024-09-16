"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!

Note: The starter code for this example is the solution.
"""

def add_five(x):
    x += 5
    return x
    
def add_five_buggy(x):
    x += 5
    
def main():
    x = 3
    print("original:", x)
    
    add_five_buggy(x)
    print("after add_five_buggy:", x)
    
    x = add_five(x)
    print("after add_five:", x)
    
if __name__ == '__main__':
    main()