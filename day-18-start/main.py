from turtle import Turtle, Screen, colormode
import random

abba_turtle = Turtle()
abba_turtle.shape('turtle')
abba_turtle.color('DarkOrchid4')


def square(points):
    for i in range(4):
        abba_turtle.forward(points)
        abba_turtle.right(90)


def dashed(reps):
    for i in range(reps):
        abba_turtle.forward(10)
        abba_turtle.pu()
        abba_turtle.forward(10)
        abba_turtle.pd()


def third_task():
    x = 4
    while x < 10:
        angle = 360 / x
        colormode(255)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        abba_turtle.pencolor((r, g, b))
        for i in range(x):
            abba_turtle.forward(50)
            abba_turtle.right(angle)
        x += 1


third_task()

screen = Screen()
screen.exitonclick()
