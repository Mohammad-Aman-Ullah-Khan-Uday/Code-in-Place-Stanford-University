from graphics import Canvas
import time
import random
import math

CANVAS_WIDTH = 500
CANVAS_HEIGHT = 600
PADDLE_Y = CANVAS_HEIGHT - 30
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 15
BALL_RADIUS = 10

BRICK_GAP = 5
BRICK_WIDTH = (CANVAS_WIDTH - BRICK_GAP*9) / 10
BRICK_HEIGHT = 10


def main():
    global change_x, change_y, canvas, window, paddle

    # Create the main 'game' window
    window = tk.Tk()
    window.protocol("WM_DELETE_WINDOW", on_closing)

    # Creates the canvas inside the window
    canvas = tk.Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()
    canvas.focus_set()

    # Bind spacebar to launch the ball
    canvas.bind("<space>", launch_ball)

    # Binds arrow keys to functions
    canvas.bind("<Left>", move_paddle_left)
    canvas.bind("<Right>", move_paddle_right)

    # Draw the bricks
    for row in range(ROWS):
        for col in range(COLUMNS):
            left_x = col * (BRICK_WIDTH + SPACING)
            top_y = row * (BRICK_HEIGHT + SPACING)
            right_x = left_x + BRICK_WIDTH
            bottom_y = top_y + BRICK_HEIGHT

            fill_color = get_brick_color(row)
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill=fill_color, tags="brick")

        # Check for victory after processing an entire row of bricks
        if not canvas.find_withtag("brick"):
            game_over(VICTORY_TEXT)

    # Draw the initial ball
    draw_circle(canvas)

    # Draw the player paddle
    paddle = player(canvas)
    print(f"Initial paddle coordinates: {canvas.coords(paddle)}")

    # Start the Tkinter event loop
    window.mainloop()


# Draws the ball and starts movement
def draw_circle(canvas):
    global change_x, change_y, ball
    x = CANVAS_WIDTH // 2
    y = CANVAS_HEIGHT // 2
    ball = canvas.create_oval(x - BALL_RADIUS, y - BALL_RADIUS, x + BALL_RADIUS, y + BALL_RADIUS, fill="black")


# Function to handle ball movement & collision detection
def move_ball():
    global change_x, change_y, ball, running, canvas, LIVES, ball_launched

    if not running or not ball_launched:
        return  # Stop if the game is not running

    # Check if ball missed the player paddle
    x1, y1, x2, y2 = canvas.coords(ball)
    if y2 >= CANVAS_HEIGHT:
        LIVES -= 1
        if LIVES == 0:
            game_over(GAME_OVER_TEXT)
        else:
            ball_launched = False
            canvas.coords(ball,
                          CANVAS_WIDTH // 2 - BALL_RADIUS,
                          CANVAS_HEIGHT // 2 - BALL_RADIUS,
                          CANVAS_WIDTH // 2 + BALL_RADIUS,
                          CANVAS_HEIGHT // 2 + BALL_RADIUS)  # Reset ball position

    left_x = x1
    top_y = y1
    right_x = x2
    bottom_y = y2

    # Check for collisions with walls
    if left_x <= 0 or right_x >= CANVAS_WIDTH:
        change_x = -change_x

    if top_y <= 0 or bottom_y >= CANVAS_HEIGHT:
        change_y = -change_y

    # Collision detection with bricks
    overlapping_items = canvas.find_overlapping(x1, y1, x2, y2)
    for item in overlapping_items:
        item_type = canvas.type(item)  # Gets the type of the object
        if item != ball:
            if item_type == "rectangle":
                if item == paddle:  # Check if it's the paddle
                    change_y = -change_y
                else:
                    brick_color = canvas.itemcget(item, "fill")
                    if brick_color != "":  # Ensure it's a brick
                        canvas.delete(item)
                        change_y = -change_y

    # Move the ball
    canvas.move(ball, change_x, change_y)
    canvas.after(int(DELAY * 1000), move_ball)  # Schedule next movement


# Draws the player paddle and return its ID
def player(canvas):
    paddle = canvas.create_rectangle(170, 390, 240, 400, fill="black")
    return paddle


# Closes window
def on_closing():
    global running, window
    running = False
    window.destroy()


def reset_ball():  # Reset ball to center when life lost.
    canvas.coords(ball,
                  CANVAS_WIDTH // 2 - BALL_RADIUS,
                  CANVAS_HEIGHT // 2 - BALL_RADIUS,
                  CANVAS_WIDTH // 2 + BALL_RADIUS,
                  CANVAS_HEIGHT // 2 + BALL_RADIUS)


def game_over(message):
    global running
    running = False
    canvas.create_text(CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2, text=message, font=("Arial", 24))


if __name__ == '__main__':
    main()