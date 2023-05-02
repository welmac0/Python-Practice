from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP = 20
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270

class SnakeBody:
    def __init__(self):
        self.body_segments = []
        self.create_snake()
        self.head = self.body_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for segment in range(len(self.body_segments) - 1, 0, -1):
            new_x = self.body_segments[segment - 1].xcor()
            new_y = self.body_segments[segment - 1].ycor()
            self.body_segments[segment].goto(new_x, new_y)
        self.body_segments[0].forward(STEP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def extend(self):
        self.add_segment(self.body_segments[-1].position())

    def add_segment(self, position):
        single_square = Turtle('square')
        single_square.penup()
        single_square.color('white')
        single_square.setposition(position)
        self.body_segments.append(single_square)