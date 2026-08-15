import turtle
from constants import SHOULD_DRAW_INSTANTLY

def setup_screen(title="My Turtle Project"):
    screen = turtle.Screen()
    screen.title(title)
    screen.tracer(0 if SHOULD_DRAW_INSTANTLY else 1)
    return screen