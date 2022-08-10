from turtle import Turtle
UP = 90
DOWN = 270


class Paddle(Turtle):  # This class creates a paddle board
    def __init__(self):
        super().__init__()
        self.paddle_body = []

    def add_segment(self, way):
        square = Turtle("square")
        square.penup()
        square.shapesize(1, 5)
        square.setheading(90)
        if way == 1:
            square.goto(-350, 0)
        if way == 2:
            square.goto(350, 0)
        square.color("white")
        square.speed("fastest")
        self.paddle_body.append(square)

    def move_up(self):  # These functions control the direction of the board
        self.paddle_body[0].setheading(UP)
        self.paddle_body[0].forward(20)

    def move_down(self):
        self.paddle_body[0].setheading(DOWN)
        self.paddle_body[0].forward(20)


