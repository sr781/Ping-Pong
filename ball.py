from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.7, 0.7)
        self.color("black")
        self.speed("fastest")
        self.reset()

    def reset(self):  # The ball is sent in a random direction
        self.goto(0, 0)
        a = random.randint(1, 2)
        if a == 2:
            self.setheading(random.randint(110, 250))
        else:
            self.setheading(random.randint(-70, 70))

    def move(self, velocity):
        self.forward(velocity)

    def direction(self, incident):
        incident = incident * -1
        self.setheading(incident)

    def paddle_bounce(self, incident):
        incident = (incident * -1) + 180
        self.setheading(incident)