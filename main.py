from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time
screen = Screen()
turtle = Turtle()
screen.tracer(0)
paddle = Paddle()
opponent = Paddle()
paddle.add_segment(1)
opponent.add_segment(2)
ball = Ball()
score = Score()
score.scoreboard(-300, 160, 0)  # Sets the position of the "Users" score
opp_score = Score()
opp_score.scoreboard(200, 160, 0)  # Sets the position of the "Opponents" score

screen.setup(width=800, height =400)  # Sets the screen width and height
screen.bgcolor("brown")
screen.listen()
screen.onkey(paddle.move_up, "w")  # Key bindings for paddle movement
screen.onkey(paddle.move_down, "s")
screen.onkey(opponent.move_up, "Up")
screen.onkey(opponent.move_down, "Down")
game_is_on = True  # As long as this boolean value is "True", the game will continue to run

while game_is_on:
    screen.update()
    time.sleep(0.001)
    if opponent.paddle_body[0].ycor() > 160:  # Stops the paddle from going out of bounds of the screen
        opponent.move_down()
    if opponent.paddle_body[0].ycor() < -140:
        opponent.move_up()
    if paddle.paddle_body[0].ycor() > 160:
        paddle.move_down()
    if paddle.paddle_body[0].ycor() < -140:
        paddle.move_up()
    ball.move(4)  # The velocity of the ball

    if ((paddle.paddle_body[0].ycor() - 50) <= ball.ycor() <= (paddle.paddle_body[0].ycor() + 50)) and ((paddle.paddle_body[0].xcor() - 20) <= ball.xcor() <= (paddle.paddle_body[0].xcor() + 20)):
        ball.paddle_bounce((ball.heading()))  # If the ball hits an area within an x and y range, the ball bounces
    if ((opponent.paddle_body[0].ycor() - 50) <= ball.ycor() <= (opponent.paddle_body[0].ycor() + 50)) and ((opponent.paddle_body[0].xcor() - 20) <= ball.xcor() <= (opponent.paddle_body[0].xcor() + 20)):
        ball.paddle_bounce((ball.heading()))
    if ball.ycor() > 200 or ball.ycor() < -200:  # If the ball hits the top or bottom, it will bounce
        ball.direction((ball.heading()))
    if ball.xcor() > 400:  # If the ball hits the edges, depending on which side it is, the score will go up and the balls position will reset
        score.scoreboard(-300, 160, 1)
        time.sleep(1)
        ball.reset()
    if ball.xcor() < -400:
        opp_score.scoreboard(200, 160, 1)
        time.sleep(1)
        ball.reset()


screen.exitonclick()