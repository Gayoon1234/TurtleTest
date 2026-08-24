import turtle

from constants import Color
from utils.screen_helper import setup_screen


def run_snake_game(screen=None):
    if screen is None:
        screen = setup_screen(
            "snake.py - Turtle Animation",
            draw_instantly=False,
            bg_color="black"
        )

    snake = turtle.Turtle()
    snake.shape("square")
    snake.color(Color.GREEN.value)
    snake.penup()
    snake.speed("fastest")

    segments = [snake]

    for position in [(20, 0), (40, 0), (60, 0), (80, 0)]:
        segment = turtle.Turtle()
        segment.shape("square")
        segment.color(Color.GREEN.value)
        segment.penup()
        segment.goto(position)
        segment.speed("fastest")
        segments.append(segment)

    def recolor_snake(color):
        for segment in segments:
            segment.color(color)

    screen.listen()
    screen.onkey(lambda: snake.setheading(90), "Up")
    screen.onkey(lambda: snake.setheading(270), "Down")
    screen.onkey(lambda: snake.setheading(180), "Left")
    screen.onkey(lambda: snake.setheading(0), "Right")
    screen.onkey(lambda: recolor_snake(Color.RED.value), "1")
    screen.onkey(lambda: recolor_snake(Color.GREEN.value), "2")
    screen.onkey(lambda: recolor_snake(Color.BLUE.value), "3")

    def move():
        for i in range(len(segments) - 1, 0, -1):
            segments[i].goto(segments[i - 1].position())

        snake.forward(20)

        screen.update()
        screen.ontimer(move, 16)

    move()
    screen.mainloop()