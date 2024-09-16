from karel.stanfordkarel import *

def turn_right():
    for i in range (3):
        turn_left()

def fill_line():
    put_beeper()
    while(front_is_clear()):
        move()
        put_beeper()

def back_to_initial_point():
    for i in range (2):
        turn_left()
    while(front_is_clear()):
        move()

def go_to_next_line():
    turn_right()
    if(front_is_clear()):
        move()
    turn_right()
    if(beepers_present()):
        while(front_is_clear()):
            move()

def main():
    while(front_is_clear()):
        fill_line()
        back_to_initial_point()
        go_to_next_line()
        
if __name__ == '__main__':
    main()