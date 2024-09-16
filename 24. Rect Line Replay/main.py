"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!

Note: The starter code for this example is the solution.
"""

import graphics

def main():
    # Makes a canvas
    canvas = graphics.create_canvas(300, 300)
    
    # Make 20 blue squares
    for i in range(20):
        value = i * 10
        
        # It can be helpful to store each coordinate into its own variable!
        left_x = value
        top_y = value
        right_x = value + 10
        bottom_y = value + 10
        
        # Create rectangle
        canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')
        
        # Keep tracks of i and prints it out
        print(i)
        
if __name__ == '__main__':
    main()