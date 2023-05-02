import turtle
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        turtle.color('white')
        turtle.penup()
        turtle.goto(0, 280)
        self.score = -1
        self.update_score()
        turtle.hideturtle()

    def update_score(self):
        self.score += 1
        turtle.clear()
        turtle.write(f"Score = {self.score}", False, 'center', ('Arial', 20, 'normal'))
        turtle.hideturtle()

    def end_game(self):
        turtle.goto(0, 0)
        turtle.clear()
        turtle.write(f"You lost with score {self.score}!", False, 'center', ('Arial', 20, 'normal'))
        turtle.hideturtle()

    def get_score(self):
        return self.score
