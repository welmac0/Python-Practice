from turtle import Screen
from snake import SnakeBody
from food import Food
from scoreboard import Scoreboard
import time

BG_COLOURS = ['black', 'blue4', 'chartreuse', 'DarkGoldenrod1', 'DarkOrchid3', 'DarkSeaGreen']

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Day 20 - snake')
screen.tracer(0)

snake = SnakeBody()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameplay = True
while gameplay:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        gameplay = False
        scoreboard.end_game()

    for segment in snake.body_segments[1:]:
        if snake.head.distance(segment) < 10:
            gameplay = False
            scoreboard.end_game()

    score = scoreboard.get_score()
    if score % 20 == 0:
        level = score / 20
        screen.bgcolor(BG_COLOURS[int(level)])

screen.exitonclick()
