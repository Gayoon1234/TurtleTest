import random
import turtle
from constants import ROYAL_COLORS
from utils.screen_helper import setup_screen

def run_spiral_2_animation(screen=None):
    if screen is None:
        screen = setup_screen("spiral2.py - Turtle Animation", draw_instantly=False)

    pen = turtle.Turtle()

    for step in range(100):
        for color in ROYAL_COLORS:
            pen.color(color)
            pen.fillcolor(color)
            pen.forward(step)
            pen.right(random.randint(20, 60))

    screen.mainloop()