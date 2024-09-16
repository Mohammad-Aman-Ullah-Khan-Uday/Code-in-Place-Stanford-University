from graphics import Canvas

# Constants for the canvas size and shapes
CANVAS_WIDTH = 150
CANVAS_HEIGHT = 150

# Outer circle's diameter and coordinates
OUTER_DIAMETER = 50
OUTER_LEFT_X = (CANVAS_WIDTH - OUTER_DIAMETER) / 2
OUTER_TOP_Y = (CANVAS_HEIGHT - OUTER_DIAMETER) / 2

# Thickness of the ring
RING_WIDTH = 10

def main():
    # Create the canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)

    # Draw the outer red oval (ring)
    canvas.create_oval(
        OUTER_LEFT_X, OUTER_TOP_Y, 
        OUTER_LEFT_X + OUTER_DIAMETER, OUTER_TOP_Y + OUTER_DIAMETER, 
        "red"
    )

    # Calculate the coordinates for the inner white oval
    inner_left_x = OUTER_LEFT_X + RING_WIDTH
    inner_top_y = OUTER_TOP_Y + RING_WIDTH
    inner_right_x = OUTER_LEFT_X + OUTER_DIAMETER - RING_WIDTH
    inner_bottom_y = OUTER_TOP_Y + OUTER_DIAMETER - RING_WIDTH

    # Draw the inner white oval to create the ring effect
    canvas.create_oval(
        inner_left_x, inner_top_y, 
        inner_right_x, inner_bottom_y, 
        "white"
    )

    # Keep the canvas open to display the drawing
    canvas.mainloop()

# Run the main function
if __name__ == '__main__':
    main()
