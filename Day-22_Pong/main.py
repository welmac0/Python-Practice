from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

LEFT_PADDLE_STARTING_POS = (-350, 0)
RIGHT_PADDLE_STARTING_POS = (350, 0)

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.listen()
screen.title('Pong')
screen.tracer(0)

paddle_right = Paddle(RIGHT_PADDLE_STARTING_POS)
paddle_left = Paddle(LEFT_PADDLE_STARTING_POS)

ball = Ball()

screen.onkey(paddle_right.down, "Down")
screen.onkey(paddle_right.up, "Up")
screen.onkey(paddle_left.down, "Left")
screen.onkey(paddle_left.up, "Right")

scoreboard = Scoreboard()

gameplay = True

while gameplay:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

    if ball.xcor() > 320 and (paddle_right.ycor() - 90 < ball.ycor() < paddle_right.ycor() + 90):
        ball.bounce_ball_horizontal()
    elif ball.xcor() > 320:
        ball.bounce_ball_horizontal()
        ball.reset_position()
        scoreboard.add_left()

    if ball.xcor() < -320 and (paddle_left.ycor() - 90 < ball.ycor() < paddle_left.ycor() + 90):
        ball.bounce_ball_horizontal()
    elif ball.xcor() < -320:
        ball.bounce_ball_horizontal()
        ball.reset_position()
        scoreboard.add_right()

screen.exitonclick()
