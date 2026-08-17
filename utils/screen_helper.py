import turtle
from constants import SHOULD_DRAW_INSTANTLY

def setup_screen(title="My Turtle Project", draw_instantly=SHOULD_DRAW_INSTANTLY):
    screen = turtle.Screen()
    screen.title(title)
    screen.tracer(0 if draw_instantly else 1)
    return screen