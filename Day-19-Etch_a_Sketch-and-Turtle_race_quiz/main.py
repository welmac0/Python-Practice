from turtle import *
import random
screen = Screen()


class EtchSketch:
    def __init__(self):
        self.my_turtle = Turtle()
        self.my_turtle.shape('arrow')
        screen.onkey(self.move_forward, 'w')
        screen.onkey(self.move_backward, 's')
        screen.onkey(self.turn_left, 'a')
        screen.onkey(self.turn_right, 'd')
        screen.onkey(self.clear_drawing, 'c')

    @staticmethod
    def move_forward(self):
        self.my_turtle.forward(10)

    @staticmethod
    def move_backward(self):
        self.my_turtle.backward(30)

    @staticmethod
    def turn_left(self):
        self.my_turtle.left(10)

    @staticmethod
    def turn_right(self):
        self.my_turtle.right(10)

    @staticmethod
    def clear_drawing(self):
        self.my_turtle.clear()
        self.my_turtle.setpos(0, 0)
        self.my_turtle.clear()


class TurtleRace:
    screen.setup(500, 400)
    user_bet = screen.textinput('Make your bet', 'Which colour of turtle will win the race? Enter a colour')
    colours = ['red', 'blue', 'green', 'purple', 'yellow', 'orange']
    turtles = []
    startingPosY = [150.0, 100.0, 50.0, -50.0, -100.0, -150.0]
    race_ongoing = False

    for i in range(len(colours)):
        newTurtle = Turtle('turtle')
        newTurtle.color(colours[i])
        newTurtle.setpos(-230.0, startingPosY[i])
        newTurtle.clear()
        turtles.append(newTurtle)

    if user_bet:
        race_ongoing = True

    while race_ongoing:
        for turtle in turtles:
            if turtle.xcor() > 230:
                race_ongoing = False
                winning = turtle.pencolor()
                if winning == user_bet:
                    print('You won!')
                else:
                    print(f'You lost. The winning colour is {winning}.')
            step = random.randint(0, 10)
            turtle.forward(step)


game = TurtleRace()
screen.exitonclick()
