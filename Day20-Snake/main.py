from turtle import Screen
from snake import SnakeBody
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Day 20 - snake')
screen.tracer(0)

snake = SnakeBody()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameplay = True
while gameplay:
    screen.update()
    time.sleep(0.2)
    snake.move()

screen.exitonclick()
