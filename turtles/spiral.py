import turtle
from constants import RGB_COLORS
from utils.screen_helper import setup_screen

def run_spiral_animation(screen=None):
    if screen is None:
        screen = setup_screen("spiral.py - Turtle Animation")

    pen = turtle.Turtle()

    for step in range(100):
        for color in RGB_COLORS:
            pen.color(color)
            pen.forward(step)
            pen.right(30)

    screen.mainloop()