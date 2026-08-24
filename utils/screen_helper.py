import turtle
from constants import SHOULD_DRAW_INSTANTLY

def setup_screen(title="My Turtle Project", draw_instantly=SHOULD_DRAW_INSTANTLY, bg_color="black"):
    screen = turtle.Screen()
    screen.title(title)
    screen.tracer(0 if draw_instantly else 1)
    screen.bgcolor(bg_color)
    return screen