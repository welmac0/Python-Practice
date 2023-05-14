from turtle import Turtle

POSITION = (0, 0)


class Ball:
    def __init__(self):
        self.ball = None
        self.create_ball()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.07

    def create_ball(self):
        self.ball = Turtle('circle')
        self.ball.penup()
        self.ball.color('white')
        self.ball.setposition(POSITION)
        self.ball.shapesize(1, 1, 1)

    def bounce_ball_vertical(self):
        self.y_move *= -1

    def bounce_ball_horizontal(self):
        self.x_move *= -1
        self.move_speed *= 0.9
        print(self.move_speed)

    def move_ball(self):
        new_x = self.ball.xcor() + self.x_move
        new_y = self.ball.ycor() + self.y_move
        self.ball.goto(new_x, new_y)

        if self.ball.ycor() > 280 or self.ball.ycor() < -280:
            self.bounce_ball_vertical()

    def ycor(self):
        return self.ball.ycor()

    def xcor(self):
        return self.ball.xcor()

    def reset_position(self):
        self.ball.setposition((0, 0))
        self.move_speed = 0.1
