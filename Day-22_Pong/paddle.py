from turtle import Turtle

WIDTH = 20
HEIGHT = 180


class Paddle:
    def __init__(self, position):
        self.paddle = None
        self.create_paddle(position)

    def create_paddle(self, position):
        self.paddle = Turtle('square')
        self.paddle.penup()
        self.paddle.color('white')
        self.paddle.setposition(position)
        self.paddle.shapesize(5, 1, 1)

    def up(self):
        if self.paddle.ycor() < 250:
            self.paddle.sety(self.paddle.ycor() + 40)

    def down(self):
        if self.paddle.ycor() > -230:
            self.paddle.sety(self.paddle.ycor() - 40)

    def xcor(self):
        return self.paddle.xcor()

    def ycor(self):
        return self.paddle.ycor()
        