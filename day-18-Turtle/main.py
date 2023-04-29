import turtle
from turtle import Turtle, Screen, colormode
import random
import colorgram

abba_turtle = Turtle()
abba_turtle.shape('turtle')
turtle.colormode(255)


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


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    returned_colour = (r, g, b)
    return returned_colour


def fourth_task():
    while True:
        abba_turtle.width(10)
        angle = 90
        step = 10
        abba_turtle.pencolor(random_colour())
        choice = random.randint(0, 2)
        if choice == 0:
            abba_turtle.forward(step)
        elif choice == 1:
            abba_turtle.left(angle)
        elif choice == 2:
            abba_turtle.right(angle)
        abba_turtle.forward(step)


def fifth_task():
    abba_turtle.speed(30)
    for i in range(36):
        abba_turtle.width(3)
        abba_turtle.pencolor(random_colour())
        abba_turtle.circle(100)
        abba_turtle.right(10)


def get_colours():
    colors = colorgram.extract('image.jpeg', 30)
    array_of_colors = []
    for i in range(len(colors)):
        array_of_colors.append((colors[i].rgb[0], colors[i].rgb[1], colors[i].rgb[2]))

    return array_of_colors


def final_task():
    step = 20
    abba_turtle.speed(10)
    abba_turtle.penup()
    abba_turtle.hideturtle()
    colours = get_colours()
    abba_turtle.forward(step)
    for i in range(1, len(colours)+1):
        set_colour = random.choice(colours)
        abba_turtle.dot(10, set_colour)
        abba_turtle.forward(step)
        if i > 0:
            if i % 10 == 0:
                abba_turtle.right(90)
                abba_turtle.forward(step)
                abba_turtle.right(90)
                abba_turtle.forward(step)
            elif i % 5 == 0:
                abba_turtle.left(90)
                abba_turtle.forward(step)
                abba_turtle.left(90)
                abba_turtle.forward(step)


final_task()

screen = Screen()
screen.exitonclick()
