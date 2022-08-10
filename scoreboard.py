from turtle import Turtle


class Score(Turtle):  # Creates a scoreboard
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.opponent_score = 0
        self.color("black")

    def scoreboard(self, x, y, point):  # This function sets the position of the scoreboard and updates everytime the score goes up by 1
        self.goto(x, y)
        self.score = self.score + point
        self.clear()
        self.write(f"Score: {self.score}", align="left", font=("Arial", 16, "normal"))