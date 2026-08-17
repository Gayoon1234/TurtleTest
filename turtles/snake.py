import random
import turtle
from constants import ROYAL_COLORS, Color
from utils.screen_helper import setup_screen

def run_snake_game(screen=None):
    if screen is None:
        screen = setup_screen("snake.py - Turtle Animation", draw_instantly=False)

    snake = turtle.Turtle()
    snake.color(Color.GREEN.value)
    snake.hideturtle()
    snake.speed('fastest')
    snake.shapesize(stretch_wid=10, stretch_len=10)
    snake.forward(20)

    def up():
        snake.setheading(90)
        snake.forward(20)

    def down():
        snake.setheading(270)
        snake.forward(20)

    def left():
        snake.setheading(180)
        snake.forward(20)

    def right():
        snake.setheading(0)
        snake.forward(20)

    screen.listen()
    screen.onkey(up, "Up")
    screen.onkey(down, "Down")
    screen.onkey(left, "Left")
    screen.onkey(right, "Right")
    

    screen.mainloop()