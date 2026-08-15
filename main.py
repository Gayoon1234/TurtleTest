import turtle
from contants import RGB_COLORS

screen = turtle.Screen()
screen.title("My Turtle Project")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)

for steps in range(100):
    for c in RGB_COLORS:
        t.color(c)
        t.forward(steps)
        t.right(30)

screen.mainloop()